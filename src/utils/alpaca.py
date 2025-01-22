import os
from dataclasses import dataclass

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


@dataclass
class AssetClass:
    us_equity = "us_equity"
    us_option = "us_option"
    crypto = "crypto"


class AuthSession(requests.Session):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.headers.update(
            {
                "APCA-API-KEY-ID": os.getenv("ALPACA_KEY"),
                "APCA-API-SECRET-KEY": os.getenv("ALPACA_SECRET"),
            }
        )


def get_all_asset_info_by_exchange(exchange: ExchangeOptions = ExchangeOptions.NYSE):
    with AuthSession() as session:
        data = session.get(f"{BASE_ASSET_URL}?status=active&exchange={exchange}")
    return data


def get_asset_info_by_symbol(symbol: str):
    with AuthSession() as session:
        data = session.get(f"{BASE_ASSET_URL}/{symbol}")
    return data
