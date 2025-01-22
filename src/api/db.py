from flask import current_app, g
from flask_sqlalchemy import SQLAlchemy

from src.models.base import Base


def init_db() -> SQLAlchemy:
    app = current_app
    if "db" not in g:
        db = SQLAlchemy(model_class=Base)
        # sqlite optimizations
        db.session.execute("""
                PRAGMA journal_mode = WAL;
                PRAGMA busy_timeout = 5000;
                PRAGMA synchronous = NORMAL;
                PRAGMA cache_size = 1000000000;
                PRAGMA foreign_keys = true;
                PRAGMA temp_store = memory;
            """)
        db.init_app(app)
    return g.db
