from pybit.unified_trading import HTTP
from dotenv import load_dotenv
import os
import pprint
import pandas as pd

load_dotenv()
api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")

session = HTTP(
    api_key=api_key,
    api_secret=api_secret,
    testnet=True,
)

def save_to_csv(data, filename='bybit_data.csv'):
    """Save API data to a CSV file."""
    try:
        if isinstance(data, list):
            df = pd.DataFrame(data)
        else:
            df = pd.DataFrame([data])
        
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving CSV: {e}")

try:
    ticker = session.get_tickers(category="linear", symbol="NEARUSDT")
    pp = pprint.PrettyPrinter(indent=0)
    pp.pprint(ticker)

    if 'result' in ticker:
        save_to_csv(ticker['result'], 'ticker.csv')
    else:
        print("Error: The ticker response does not contain 'result'.")

except Exception as e:
    print(f"Error fetching ticker data: {e}")

try:
    order_book = session.get_orderbook(category="linear", symbol="NEARUSDT")
    pp = pprint.PrettyPrinter(indent=0)
    pp.pprint(order_book)

    if 'result' in order_book:
        save_to_csv(order_book['result'], 'order_book.csv')
    else:
        print("Error: The order book response does not contain 'result'.")

except Exception as e:
    print(f"Error fetching order book: {e}")
