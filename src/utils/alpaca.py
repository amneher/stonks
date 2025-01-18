from dataclasses import dataclass
import os
import requests


BASE_ASSET_URL = "https://api.alpaca.markets/v2/assets"


@dataclass
class ExchangeOptions:
    AMEX = "AMEX"
    ARCA = "ARCA"
    BATS = "BATS"
    NYSE = "NYSE"
    NASDAQ = "NASDAQ"
    NYSEARCA = "NYSEARCA"
    OTC = "OTC"


class AuthSession(requests.Session):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.headers.update({
            "APCA-API-KEY-ID": os.getenv("ALPACA_KEY"),
            "APCA-API-SECRET-KEY": os.getenv("ALPACA_SECRET")
        })


def get_all_asset_info_by_exchange(exchange: ExchangeOptions = ExchangeOptions.NYSE):  # NOQA: E501
    with AuthSession() as session:
        data = session.get(f"{BASE_ASSET_URL}?status=active&exchange={exchange}")  # NOQA: E501
    return data


def get_asset_info_by_symbol(symbol: str):
    with AuthSession() as session:
        data = session.get(f"{BASE_ASSET_URL}/{symbol}")
    return data
