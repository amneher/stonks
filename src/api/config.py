from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATABASE_FILE = BASE_DIR / "stonks.db"
SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_FILE}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"
