

from src.models.base import Base

asset_info_fields =  'margin_requirement_long', 'margin_requirement_short', 'shortable', 'easy_to_borrow', 'fractionable', 'attributes', 'min_order_size', 'min_trade_increment', 'price_increment']


class Asset(Base):
    __tablename__ = "assets"
    id: str     # uuid/str?
    asset_class: str  # choices: us_equity, crypto
    exchange: str   # exchange choices cf. alpaca.py
    symbol: str 
    name: str
    status: str  # choices: active, ...
    tradable: str  # bool
    marginable: str # bool
    maintenance_margin_requirement: int
    margin_requirement_long: int
    margin_requirement_short: int
    shortable: bool
    easy_to_borrow: bool
    fractionable: bool
    attributes: str  # list[str]
    min_order_size: str  # optional float
    min_trade_increment: str  # optional float
    price_increment: str  # optional float