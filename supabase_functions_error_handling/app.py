import os

from dotenv import load_dotenv
from supabase import Client, create_client, FunctionsError

load_dotenv()

url = os.environ.get("SUPABASE_URL", "")
key = os.environ.get("SUPABASE_KEY", "")


supabase: Client = create_client(url, key)

try:
    response = supabase.functions.invoke("hello")

    print(f"RESPONSE: {response}")
except FunctionsError as e:
    err = e.to_dict()
    print(e.to_dict())
