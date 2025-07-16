from aiorun import run
import os
import logging
import datetime
from dotenv import load_dotenv
from supabase import AClient, acreate_client

load_dotenv()

url = os.environ.get("SUPABASE_URL", "")
key = os.environ.get("SUPABASE_KEY", "")

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.WARNING)

async def create_supabase():
    supabase: AClient = await acreate_client(url, key)
    return supabase


async def test_broadcast(supabase):
    channel = supabase.channel("test-channel")

    def message_received(payload):
        time_now = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        logger.warning(f"broadcast: {time_now} -> {payload}")

    await channel.on_broadcast("heartbeat", message_received).subscribe()


async def main():
    logger.warning('Started')
    supabase = await create_supabase()
    await test_broadcast(supabase)


if __name__ == "__main__":
    run(main())
