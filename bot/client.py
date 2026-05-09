from binance.client import Client
from dotenv import load_dotenv
import os
import time

load_dotenv()

def get_client():

    api_key = os.getenv("BINANCE_API_KEY")
    secret_key = os.getenv("BINANCE_SECRET_KEY")

    client = Client(
        api_key,
        secret_key,
        testnet=True
    )

    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    # Sync local timestamp with Binance server
    server_time = client.get_server_time()
    client.timestamp_offset = server_time['serverTime'] - int(time.time() * 1000)

    return client