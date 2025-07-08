import requests
import os
from dotenv import load_dotenv
load_dotenv()

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")

def get_contract_events(address, network="ethereum"):
    if network == "ethereum":
        base_url = "https://api.etherscan.io/api"
    elif network == "polygon":
        base_url = "https://api.polygonscan.com/api"
    else:
        raise ValueError("Unsupported network")

    params = {
        "module": "logs",
        "action": "getLogs",
        "fromBlock": "latest",
        "address": address,
        "apikey": ETHERSCAN_API_KEY
    }

    response = requests.get(base_url, params=params)
    return response.json()

def get_token_price(token_id="ethereum"):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": token_id, "vs_currencies": "usd"}
    response = requests.get(url, params=params)
    return response.json()

print(get_token_price("uniswap"))