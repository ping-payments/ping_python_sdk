from locale import currency
import os
from dotenv import load_dotenv
from ping.payments_api import PaymentsApi
import random

from faker import Faker
fake = Faker(['no_NO', 'sv_SE', 'en_US'])

customer = {
    "email": fake.free_email(),
    "first_name": fake.first_name(),
    "last_name": fake.last_name(),
    "phone": fake.phone_number()
}
items = [
    {
        "description": random.choice(["Hawaii Pizza", "Margarita", "Vesuvio", "Altono"]),
        "merchant_id": os.getenv("MERCHANT_ID"),
        "price": random.choice([1000, 3500, 4000, 4500]),
        "quantity": random.randint(1, 5),
        "vat": random.choice([0, 6, 12, 25])
    }
]
supplier = {
    "city": fake.city(),
    "name": fake.company(),
    "organization_number": str(random.randint(0000000000, 9999999999)),
    "website": fake.domain_name(),
    "zip": str(random.randint(00000, 99999))
}
swish_parameters = [
    {
        "method": "e_commerce",
        "parameters": {
            "swish_message": "Pizza from the pizzeria"
        },
        "provider": "swish"
    }
]
complete_create_body = {
    "customer": customer,
    "items": items,
    "locale": "sv-SE",
    "payment_order_id": os.getenv("PAYMENT_ORDER_ID"),
    "payment_provider_methods": swish_parameters,
    "supplier": supplier,
    "currency": "SEK",
    "total_amount": int(items[0]["price"]) * int(items[0]["quantity"])
}


print(items[0])


"""
tenant_id = os.getenv("TENANT_ID")
payments_api = PaymentsApi(tenant_id)

split_tree_id = os.getenv("SPLIT_TREE_ID")
result = payments_api.paymentOrder.create(split_tree_id, "SEK")

if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
    print("error")"""
