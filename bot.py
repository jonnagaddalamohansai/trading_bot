# bot.py
import os
from dotenv import load_dotenv
from pybit.unified_trading import HTTP

load_dotenv()

api_key = os.getenv("BYBIT_API_KEY")
api_secret = os.getenv("BYBIT_API_SECRET")

client = HTTP(
    testnet=True,
    api_key=api_key,
    api_secret=api_secret
)

def place_order(symbol, side, order_type, qty, price=None):
    try:
        category = "spot"  # or "linear" for futures

        time_in_force = "GoodTillCancel" if category == "linear" else "IOC"

        order_payload = {
            "category": category,
            "symbol": symbol,
            "side": side.upper(),
            "order_type": order_type.upper(),
            "qty": str(qty),
            "time_in_force": time_in_force,
        }

        if order_type == "limit" and price is not None:
            order_payload["price"] = str(price)

        response = client.place_order(**order_payload)

        if response.get("retCode") == 0:
            print("✅ Order placed successfully!")
        else:
            print(f"❌ Error placing order: {response.get('retMsg')}")
            print(f"Request → {order_payload}")
            print(response)

    except Exception as e:
        print(f"❌ Exception while placing order: {e}")
