import os

from dotenv import load_dotenv
from fastapi import Body, FastAPI, Depends
from supabase import AClient, acreate_client
from postgrest import APIError

load_dotenv()

url = os.environ.get("SUPABASE_URL", "")
key = os.environ.get("SUPABASE_KEY", "")
service_key = os.environ.get("SUPABASE_SERVICE_KEY", "")

app = FastAPI()

async def get_supabase_client():
    supabase = await acreate_client(
        url, service_key
    )
    return supabase

@app.get("/list-users")
async def list_users(supabase: AClient = Depends(get_supabase_client)):
    """A route that uses Supabase."""
    res = await supabase.auth.admin.list_users()
    return res

@app.post("/delete-user")
async def delete_user(supabase: AClient = Depends(get_supabase_client), id: str = Body(...),):
    """A route that uses Supabase."""
    await supabase.auth.admin.delete_user(id)
    return {"message": f"User ({id}) successfully deleted"}

@app.post("/add-user")
async def add_user(supabase: AClient = Depends(get_supabase_client)):
    """A route that uses Supabase."""
    res = await supabase.auth.admin.create_user({
        "email": "hello@example.com",
        "password": "password123",
        "email_confirm": True
    })
    return res
