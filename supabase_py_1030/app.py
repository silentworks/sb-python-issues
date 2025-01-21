import os

from dotenv import load_dotenv
from supabase import Client, create_client
from postgrest import APIError

load_dotenv()

url = os.environ.get("SUPABASE_URL", "")
key = os.environ.get("SUPABASE_KEY", "")


supabase: Client = create_client(url, key)

user = supabase.auth.sign_in_with_password(
    {"email": "up+rosamond_damore@example.com", "password": "password123"}
)

try:
    response = supabase.table("countries").insert({"name": "Jamaica"}).execute()

    print(f"RESPONSE: {response}")
except APIError as e:
    print(f"ERROR: {e}")
