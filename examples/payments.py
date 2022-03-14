from unittest import result
from ping.payments_api import PaymentsApi

def initiate_payment():
  tenant_id = "a2a4f648-a50b-42fb-bda8-00c6e2f295ea"
  payments_api = PaymentsApi(tenant_id=tenant_id)
  payment_order_id = "8a6a4586-e082-49fe-b408-b92e9dc746ec"

  payment_object = {
     "currency": "SEK",
    "merchant_amounts": {
      "075b5c3c-3f17-435d-ab84-0bc57d8e67d4": 9400,
    },
    "metadata": {
      "delivery_id": "368745"
    },
    "method": "mobile",
    "order_items": [
      {
        "amount": 2500,
        "name": "Utkörning, Marios Pasta (Pasta La Vista)",
        "vat_rate": 12
      },
      {
        "amount": 6900,
        "name": "Marios Pasta (Pasta La Vista)",
        "vat_rate": 12
      }
    ],
    "provider": "swish",
    "provider_method_parameters": {
      "message": "Marios Pasta från Pasta La Vista",
      "phone_number": "0700000000"
    },
    "status_callback_url": "https://somesite.com/callback"
  }
  result = payments_api.payment.initiate_payment(payment_object, payment_order_id)
  if result.is_success():
    print(result.body)
    print("success")
  elif result.is_error():
    print(result.errors)
    print(result.status_code)
    print("error")

def get_payment():
  tenant_id = "a2a4f648-a50b-42fb-bda8-00c6e2f295ea"
  payments_api = PaymentsApi(tenant_id=tenant_id)
  
  paymen_order_id = "8a6a4586-e082-49fe-b408-b92e9dc746ec"
  payment_id = "c498dba8-bf28-4252-a16a-7c6192c05bc9"

  result = payments_api.payment.get_payment(paymen_order_id, payment_id)
  if result.is_success():
    print(result.body)
    print("success")
  elif result.is_error():
    print(result.errors)
    print(result.status_code)
    print("error")

initiate_payment()