from pybit.unified_trading import HTTP
from dotenv import load_dotenv
import os
import pprint
import time
import pandas as pd

load_dotenv()
api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")

session = HTTP(
    api_key=api_key,
    api_secret=api_secret,
    testnet=True,
)  

def bybit_csv(data, filename='dados_bybit.csv'):
    try:
        if isinstance(data, list):
            df = pd.DataFrame(data)
        else:
            df = pd.DataFrame([data])
        
        df.to_csv(filename, index=False)
        print(f"Dados salvos em {filename}")
    except Exception as e:
        print(f"Erro ao salvar em CSV: {e}")

#market informations
try:
    ticker = session.get_tickers(category="linear", symbol="NEARUSDT")
    pp = pprint.PrettyPrinter(indent=0)
    pp.pprint(ticker)

    if 'result' in ticker:
        bybit_csv(ticker['result'], 'ticker.csv')
    else:
        print("Erro: O ticker não contém a chave 'result'.")

except Exception as e:
    print(f"Erro ao buscar ticker: {e}")

#order book informations
try:
    order_book = session.get_orderbook(category="linear", symbol="NEARUSDT")
    pp = pprint.PrettyPrinter(indent=0)
    print(order_book)

    if 'result' in order_book:
        bybit_csv(order_book['result'], 'order_book.csv')
    else:
        print("Erro: Não existe 'result' em order book.")

except Exception as e:
    print(f"Erro ao buscar order book: {e}")

