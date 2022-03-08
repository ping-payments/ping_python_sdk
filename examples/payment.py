from ping.tenant import Tenant
def initiate_payment():
  tenant_id = "a2a4f648-a50b-42fb-bda8-00c6e2f295ea"
  tenant = Tenant(tenant_id= tenant_id)
  payment_order_id = "bd3e750f-2213-45c5-9d02-0dbeb2178675"

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
  status = tenant.initiate_payment(payment_object, payment_order_id)
  print(status.text)
  print(status.status_code)

def get_payment():
  tenant_id = "a2a4f648-a50b-42fb-bda8-00c6e2f295ea"
  tenant = Tenant(tenant_id= tenant_id)
  
  paymen_order_id = "bd3e750f-2213-45c5-9d02-0dbeb2178675"
  payment_id = "9e6333c6-a9c3-4883-98d8-1f9ef6f1955b"

  payment = tenant.get_payment(paymen_order_id, payment_id)
  print(payment.text)
  print(payment.status_code)

get_payment()