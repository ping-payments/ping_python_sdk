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
  "method": "dummy",
  "order_items": [
        {
            "amount": 2500,
            "merchant_id": os.getenv("MERCHANT_ID"),
            "name": "Delivery, Marios Pasta (Pasta La Vista)",
            "vat_rate": 12
        }
    ],
    "provider": "dummy",
    "provider_method_parameters": {
        "desired_payment_status": "COMPLETED"
    },
    "status_callback_url": "https://somesite.com/callback"
}

result = payments_api.payment.initiate_payment(payment_object, payment_order_id)

if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.status_code)
    print(result.errors)
    print("error")
