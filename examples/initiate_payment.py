import os
from dotenv import load_dotenv
from ping.payments_api import PaymentsApi

load_dotenv()

tenant_id = os.getenv("TENANT_ID")
payments_api = PaymentsApi(tenant_id)

payment_order_id = os.getenv("PAYMENT_ORDER_ID")
payment_object = {
    "currency": "SEK",
    "metadata": {
        "delivery_id": "368745"
    },
    "total_amount": 2500,
    "method": "e_commerce",
    "order_items": [
        {
            "amount": 2500,
            "merchant_id": os.getenv("MERCHANT_ID"),
            "name": "Delivery, Marios Pasta (Pasta La Vista)",
            "vat_rate": 12
        }
    ],
    "provider": "swish",
    "provider_method_parameters": {
        "phone_number": "0700000000",
        "message": "example text"
    }
}

result = payments_api.payment.initiate(payment_object, payment_order_id)

if result.is_success():
    print(f"Success: \n {result.body}")
elif result.is_error():
    print(f"Error: {result.status_code} \n {result.errors}")
