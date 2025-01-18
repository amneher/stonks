"""
    Main entrypoint for the stock info collector & advisor.
"""
import os
from flask import Flask
from dotenv import load_dotenv
from utils.database import query_db
from utils import alpaca


load_dotenv()

app = Flask(__name__)


@app.route('/')
def get_sample(symbols: list[str] = ["AAPL", "TSLA"]):
    data = []
    for symbol in symbols:
        # get today's market data
        df = alpaca.get_recent_symbol_bars(symbol)
        data.append(df)
    return data


def start():
    """ the function to start it all. """
    api_port_str = os.environ.get("API_PORT", default=None)
    api_port = int(api_port_str) if api_port_str is not None else None
    app.run(port=api_port)


if __name__ == "__main__":
    start()
