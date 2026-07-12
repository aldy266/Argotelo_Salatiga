import os
from pathlib import Path
from urllib.parse import quote_plus

import certifi
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent

# Local development may use .env in the project root or Backend/.env.
# Vercel injects environment variables directly at build/runtime.
load_dotenv(PROJECT_ROOT / ".env", override=False)
load_dotenv(BASE_DIR / ".env", override=True)


def _env(name, default=None):
    value = os.getenv(name)
    if value is None or value == "":
        return default
    return value


def _env_bool(name, default=False):
    value = _env(name)
    if value is None:
        return default
    return str(value).strip().lower() in {"1", "true", "yes", "on"}


def _build_database_uri():
    settings = {
        "DB_HOST": _env("DB_HOST"),
        "DB_PORT": _env("DB_PORT", "4000"),
        "DB_USER": _env("DB_USER"),
        "DB_PASSWORD": _env("DB_PASSWORD"),
        "DB_NAME": _env("DB_NAME"),
    }

    missing = [name for name, value in settings.items() if not value]
    if not missing:
        return (
            "mysql+pymysql://"
            f"{quote_plus(settings['DB_USER'])}:{quote_plus(settings['DB_PASSWORD'])}@"
            f"{settings['DB_HOST']}:{settings['DB_PORT']}/"
            f"{quote_plus(settings['DB_NAME'])}?charset=utf8mb4"
        )

    if os.getenv("VERCEL"):
        raise RuntimeError(
            "Environment variable database belum lengkap: " + ", ".join(missing)
        )

    local_db = BASE_DIR / "instance" / "argotelo_dev.sqlite3"
    local_db.parent.mkdir(exist_ok=True)
    return "sqlite:///" + local_db.as_posix()


def _engine_options(database_uri):
    if database_uri.startswith("mysql+pymysql://"):
        return {
            "connect_args": {
                "ssl": {
                    "ca": certifi.where()
                }
            },
            "pool_pre_ping": True,
            "pool_recycle": 280,
            "pool_timeout": 30,
        }

    return {"pool_pre_ping": True}


_DATABASE_URI = _build_database_uri()
_SECRET_KEY = _env("SECRET_KEY", "argotelo-dev-secret")

if os.getenv("VERCEL") and _SECRET_KEY == "argotelo-dev-secret":
    raise RuntimeError("SECRET_KEY wajib diisi pada Environment Variables Vercel")


class Config:
    SECRET_KEY = _SECRET_KEY
    SQLALCHEMY_DATABASE_URI = _DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = _engine_options(_DATABASE_URI)

    MAX_CONTENT_LENGTH = int(_env("MAX_UPLOAD_SIZE", 5 * 1024 * 1024))
    POS_TAX_RATE = float(_env("POS_TAX_RATE", 0.10))

    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = _env_bool("SESSION_COOKIE_SECURE", bool(os.getenv("VERCEL")))
    PREFERRED_URL_SCHEME = "https" if os.getenv("VERCEL") else "http"

    AUTO_INIT_DB = _env_bool("AUTO_INIT_DB", False)

    MIDTRANS_SERVER_KEY = _env("MIDTRANS_SERVER_KEY")
    MIDTRANS_CLIENT_KEY = _env("MIDTRANS_CLIENT_KEY")
    MIDTRANS_IS_PRODUCTION = _env_bool("MIDTRANS_IS_PRODUCTION", False)
    MIDTRANS_SNAP_URL = (
        "https://app.midtrans.com/snap/snap.js"
        if MIDTRANS_IS_PRODUCTION
        else "https://app.sandbox.midtrans.com/snap/snap.js"
    )
