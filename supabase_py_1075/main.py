import os
from fastapi import FastAPI, Depends
from supabase import AsyncClient as Client, acreate_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_ANON_KEY = os.environ.get("SUPABASE_KEY", "")

app = FastAPI()


# Dependency that creates a new Supabase client per request
async def get_supabase_client():
    supabase = await acreate_client(
        SUPABASE_URL, SUPABASE_ANON_KEY
    )  # Creates a new client per request
    return supabase


@app.get("/")
async def test_supabase(supabase: Client = Depends(get_supabase_client)):
    """A route that uses Supabase."""
    res = await supabase.table("cities").select("*").limit(1).execute()
    return res
