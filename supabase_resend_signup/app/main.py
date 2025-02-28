import os
from dotenv import load_dotenv
from supabase import AsyncClient, acreate_client, AsyncClientOptions as ClientOptions
from fastapi import FastAPI, Body, Depends, Request, HTTPException
from typing import Optional
import uuid
from starlette.middleware.sessions import SessionMiddleware
from gotrue.types import VerifyTokenHashParams, EmailOtpType
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


async def create_supabase(request: Request) -> AsyncClient:
    return await acreate_client(
        url,
        key,
        options=ClientOptions(
            storage=FastApiSessionStorage(request.session),
        ),
 
    )

app = FastAPI(title="Signout with scope")
app.add_middleware(
    SessionMiddleware,
    secret_key="c8af43a9a0609678800db3c5a3a8d179f386e083f559518f2528202a4b7de8f8",
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/signin')
async def sign_in(
    supabase: AsyncClient = Depends(create_supabase),
    email: str = Body(default="up+rosamond_damore@example.com"),
    password: str = Body(default="password123"),
):
    try:
        user = await supabase.auth.sign_in_with_password(
            credentials={"email": email, "password": password}
        )

        if user:
            return {"message": "User signed in successfully", "user": user}
    except (AuthApiError, AuthInvalidCredentialsError) as exception:
        err = exception.to_dict()
        return {
            "error": err.get("message"),
        }

@app.post('/signup')
async def sign_up(
    supabase: AsyncClient = Depends(create_supabase),
    email: str = Body(default="up+rosamond_damore@example.com"),
    password: str = Body(default="password123"),
):
    try:
        user = await supabase.auth.sign_up(
            credentials={"email": email, "password": password}
        )

        if user:
            return {"message": "User signed up successfully", "user": user}
    except (AuthApiError, AuthInvalidCredentialsError) as exception:
        err = exception.to_dict()
        return {
            "error": err.get("message"),
        }

@app.post('/resend')
async def resend(
    supabase: AsyncClient = Depends(create_supabase),
    email: str = Body(default="up+rosamond_damore@example.com"),
    type: str = "signup",
):
    try:
        await supabase.auth.resend(
            credentials={"email": email, "type": type}
        )

        return {"message": "Resent confirmation email successfully"}
    except (AuthApiError, AuthInvalidCredentialsError) as exception:
        err = exception.to_dict()
        return {
            "error": err.get("message"),
        }


@app.get("/confirm")
async def confirm(
    request: Request,
    token_hash: str,
    type: EmailOtpType = "email",
    supabase: AsyncClient = Depends(create_supabase),
):
    try:
        if token_hash and type:
            await supabase.auth.verify_otp(
                params={"token_hash": token_hash, "type": type}
            )

        return {"message": "User signed in successfully."}
    except AuthApiError as exception:
        err = exception.to_dict()
        return {"message": err.get("message"), "error": True}


@app.post("/verify-token")
async def verify_token(
    request: Request,
    supabase: AsyncClient = Depends(create_supabase),
    email: str = Body(...),
    token: str = Body(...),
    type: EmailOtpType = Body(default="email_change"),
):
    try:
        response = await supabase.auth.verify_otp(
            params={"email": email, "token": token, "type": type}
        )
        return response
    except AuthApiError as exception:
        err = exception.to_dict()
        return {"message": err.get("code"), "error": True}

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


