"""
Main entrypoint for the stock info collector & advisor.
"""

from dotenv import load_dotenv
from flask import Blueprint

from src.api import create_app
from src.api.auth import login_required
from src.api.db import init_db
from utils import alpaca

load_dotenv()
db = init_db()
bp = Blueprint("main", __name__, url_prefix="/")


@login_required
@bp.route("/", methods=("GET",))
def index():
    data = alpaca.asset_info_by_exchange()

    return data  # TODO: serialize it.


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
