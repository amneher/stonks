from typing import Annotated

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.api.db import init_db

db = init_db()

intpk = Annotated[int, mapped_column(primary_key=True)]


class User(db.Model):
    __tablename__ = "users"
    id: Mapped[intpk] = mapped_column(init=False)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    email: Mapped[str]
    password: Mapped[str] = mapped_column(String(100), nullable=False)
