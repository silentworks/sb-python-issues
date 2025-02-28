import os
import logging
from dotenv import load_dotenv
from supabase import AsyncClient, acreate_client, AsyncClientOptions as ClientOptions
from fastapi import FastAPI, Body, Depends, Request, HTTPException
from typing import Optional
import uuid
from starlette.middleware.sessions import SessionMiddleware
from gotrue.errors import (
    AuthApiError,
    AuthInvalidCredentialsError,
    AuthWeakPasswordError,
)
from .fastapi_storage import FastApiSessionStorage

load_dotenv()

url = os.environ.get("SUPABASE_URL", "")
key = os.environ.get("SUPABASE_KEY", "")
service_key = os.environ.get("SUPABASE_SERVICE_KEY", "")

# Configure logging
logging.basicConfig(level=logging.DEBUG)

async def create_supabase(request: Request) -> AsyncClient:
    return await acreate_client(
        url,
        key,
        options=ClientOptions(
            storage=FastApiSessionStorage(request.session),
        ),
 
    )

app = FastAPI(title="Signup with phone and password")
app.add_middleware(
    SessionMiddleware,
    secret_key="c8af43a9a0609678800db3c5a3a8d179f386e083f559518f2528202a4b7de8f8",
)

@app.get("/")
async def root():
    return {"message": "Go to http://127.0.0.1:8000/docs"}

@app.get("/session")
async def logged_in_session(
    supabase: AsyncClient = Depends(create_supabase),
):
    try:
        response = await supabase.auth.get_session()
        return {"message": "Retrieving session", "response": response}
    except AuthApiError as exception:
        err = exception.to_dict()
        return {"message": err.get("message"), "error": True, "err": err}

@app.get("/user")
async def logged_in_user(
    supabase: AsyncClient = Depends(create_supabase),
):
    try:
        response = await supabase.auth.get_user()
        return {"message": "Retrieving user", "response": response}
    except AuthApiError as exception:
        err = exception.to_dict()
        return {"message": err.get("message"), "error": True, "err": err}

@app.post('/signup')
async def sign_up(
    supabase: AsyncClient = Depends(create_supabase),
    phone: str = Body(default="4152127777"),
    password: str = Body(default="password123"),
):
    try:
        user = await supabase.auth.sign_up(
            credentials={"phone": phone, "password": password, "options": {"channel": "sms"}}
        )

        if user:
            return {"message": "User signed in successfully", "user": user}
    except (AuthApiError, AuthInvalidCredentialsError) as exception:
        err = exception.to_dict()
        return {
            "error": err.get("message"),
        }



@app.post('/signin')
async def sign_in(
    supabase: AsyncClient = Depends(create_supabase),
    phone: str = Body(default="4152127777"),
    password: str = Body(default="password123"),
):
    try:
        user = await supabase.auth.sign_in_with_password(
            credentials={"phone": phone, "password": password, "options": {"channel": "sms"}}
        )

        if user:
            return {"message": "User signed in successfully", "user": user}
    except (AuthApiError, AuthInvalidCredentialsError) as exception:
        err = exception.to_dict()
        return {
            "error": err.get("message"),
        }


@app.post("/signout")
async def sign_out(
    supabase: AsyncClient = Depends(create_supabase),
    scope: str = Body(default="global")
):
    try:
        await supabase.auth.sign_out({"scope": scope})
    except AuthApiError as message:
        return {"error": message}
    return {"message": "You have successfully signed out"}


