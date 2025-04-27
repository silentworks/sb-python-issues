import os
from fastapi import FastAPI, Depends
from httpx import AsyncClient, AsyncHTTPTransport, Limits, Timeout
from supabase import AsyncClient as Client, AsyncClientOptions, acreate_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_ANON_KEY = os.environ.get("SUPABASE_KEY", "")

app = FastAPI()


# Dependency that creates a new Supabase client per request
async def get_supabase_client():
    supabase = await acreate_client(
        SUPABASE_URL, SUPABASE_ANON_KEY,
        # options=AsyncClientOptions(postgrest_client_timeout=Timeout(None))
    )  # Creates a new client per request
    return supabase

async def get_supabase_httpx_client():
    transport = AsyncHTTPTransport(
        retries=10,
        http2=True,
        limits=Limits(
            max_connections=1,
            max_keepalive_connections=1,
            keepalive_expiry=None,
        )
    )
    client = AsyncClient(transport=transport)
    supabase = await acreate_client(
        SUPABASE_URL, SUPABASE_ANON_KEY,
        options=AsyncClientOptions(httpx_client=client)
    )  # Creates a new client per request
    return supabase


@app.get("/")
async def test_supabase(supabase: Client = Depends(get_supabase_client)):
    """A route that uses Supabase."""
    res = await supabase.table("cities").select("*").limit(1).execute()
    return res

@app.get("/s/httpx")
async def test_supabase_httpx(supabase: Client = Depends(get_supabase_httpx_client)):
    """A route that uses Supabase."""
    res = await supabase.table("cities").select("*").limit(1).execute()
    return res

@app.get("/httpx")
async def test_httpx():
    """A route that uses Supabase."""
    transport = AsyncHTTPTransport(
        retries=3,
        http2=True,
        limits=Limits(
            max_connections=100,
            max_keepalive_connections=1,
            keepalive_expiry=None,
        )
    )
    headers = {"Authorization": f"Bearer {SUPABASE_ANON_KEY}", "apiKey": SUPABASE_ANON_KEY, "Connection": "close"}
    async with AsyncClient(
        transport=transport,
        headers=headers,
        base_url=f"{SUPABASE_URL}/rest/v1",
        http2=True
    ) as client:
        res = await client.request(
            "GET",
            "/cities",
            params={"select": "*", "limit": 1},
            timeout=None
        )

    return res.json()
