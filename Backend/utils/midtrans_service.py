import os
from pathlib import Path

import midtransclient
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[1]
PROJECT_ROOT = BASE_DIR.parent

load_dotenv(PROJECT_ROOT / ".env", override=False)
load_dotenv(BASE_DIR / ".env", override=True)


def _is_production():
    return str(os.getenv("MIDTRANS_IS_PRODUCTION", "false")).strip().lower() in {
        "1", "true", "yes", "on"
    }


def _snap_client():
    server_key = os.getenv("MIDTRANS_SERVER_KEY")
    if not server_key:
        raise RuntimeError("MIDTRANS_SERVER_KEY belum dikonfigurasi")

    return midtransclient.Snap(
        is_production=_is_production(),
        server_key=server_key,
    )


def create_payment(order_id, total, customer):
    parameter = {
        "transaction_details": {
            "order_id": order_id,
            "gross_amount": int(total),
        },
        "customer_details": {
            "first_name": customer,
        },
    }

    transaction = _snap_client().create_transaction(parameter)
    return transaction["token"]
