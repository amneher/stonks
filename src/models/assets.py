from typing import Annotated, List, Optional

from sqlalchemy import String  # , Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.api.db import init_db
from src.utils.alpaca import AssetClass, ExchangeOptions, get_all_asset_info_by_exchange

db = init_db()

str5 = Annotated[str, mapped_column(String(5))]
str10 = Annotated[str, mapped_column(String(10))]
str40 = Annotated[str, mapped_column(String(40))]
true_bool = Annotated[bool, mapped_column(default=True)]


class Asset(db.Model):
    __tablename__ = "assets"
    id: Mapped[str40] = mapped_column(primary_key=True, init=True)
    asset_class: Mapped[AssetClass] = mapped_column(default=AssetClass.us_equity)
    exchange: Mapped[ExchangeOptions] = mapped_column(default=ExchangeOptions.NYSE)
    symbol: Mapped[str10]
    name: Mapped[str40]
    status: Mapped[true_bool]
    tradable: Mapped[true_bool]
    marginable: Mapped[true_bool]
    shortable: Mapped[true_bool]
    easy_to_borrow: Mapped[true_bool]
    fractionable: Mapped[true_bool]
    margin_requirement_long: Mapped[Optional[str5]]
    margin_requirement_short: Mapped[Optional[str5]]
    attributes: Mapped[Optional[List[str]]]


def asset_info_by_exchange(exchange: ExchangeOptions = ExchangeOptions.NYSE):
    # if not in cache, check db. if not in db, load from api.
    assets: List[Asset] = db.session.execute(
        db.select(Asset).filter_by(exchange=exchange)
    )
    if not assets:
        asset_data = get_all_asset_info_by_exchange(exchange)
        for asset in asset_data:
            assets.append(Asset(asset))
        db.session.add_all(assets)
        db.session.commit()
    return assets
