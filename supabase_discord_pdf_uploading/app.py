import os

from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv()

url = os.environ.get("SUPABASE_URL", "")
key = os.environ.get("SUPABASE_KEY", "")


supabase: Client = create_client(url, key)

try:
    file_path = "upload/sample_explain.pdf"
    # Read file content
    with open("./c4611_sample_explain.pdf", "rb") as file:
        # Upload to Supabase storage
        result = supabase.storage.from_('user_pdfs').upload(
            path=file_path,
            file=file,
            file_options={"content-type": "application/pdf"}
        )

    response = supabase.storage.from_('user_pdfs').get_public_url(file_path)

    print(f"RESPONSE: {response}")
except APIError as e:
    print(f"ERROR: {e}")
