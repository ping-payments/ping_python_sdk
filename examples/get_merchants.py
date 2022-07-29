
import os
from dotenv import load_dotenv
from ping.payment_links_api import PaymentLinksApi


load_dotenv()
tenant_id = "a2a4f648-a50b-42fb-bda8-00c6e2f295ea"
print(tenant_id)
payment_links_api = PaymentLinksApi(tenant_id)

request = {
    "customer": {
        "email": "some.email@domain.com",
        "first_name": "Bertil",
        "last_name": "Jönsson",
        "phone": "0700000000"
      },
      "delivery_address": {
        "city": "Örebro",
        "street_address": "Nygatan 15",
        "zip": "702 10"
      },
      "due_date": "2022-03-25",
      "invoice_address": {
        "city": "Örebro",
        "street_address": "Nygatan 15",
        "zip": "702 10"
      },
      "items": [
        {
          "description": "Hawaii Pizza",
          "merchant_id": os.getenv("MERCHANT_ID"),
          "price": 7000,
          "quantity": 2,
          "vat": 12
        }
      ],
      "locale": "sv-SE",
      "logo_image_link": "https://someurl.com/some-image.png",
      "payment_link_status_callback_url": "https://someurl.com/payment_link_callback",
      "payment_order_id": os.getenv("PAYMENT_ORDER_ID"),
      "payment_provider_methods": [
        {
          "method": "e_commerce",
          "parameters": {
            "swish_message": "Tack för din betalning"
          },
          "provider": "swish"
        }
      ],
      "supplier": {
        "city": "Örebro",
        "name": "name",
        "organization_number": "5555555555",
        "website": "https://somewebsite.com",
        "zip": "45133"
      },
      "currency": "SEK",
      "total_amount": 14000
    }
response = payment_links_api.payment_links.create(request)
print(response)
