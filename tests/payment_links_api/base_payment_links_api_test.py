import unittest
import os
from tests.test_helper import TestHelper
from ping.payment_links_api import PaymentLinksApi


class BasePaymentLinksApiTest(unittest.TestCase):

    def setUp(self):
        self.test_helper = TestHelper
        self.payment_links_api = PaymentLinksApi(os.getenv("TENANT_ID"))
        self.merchant_id = os.getenv("MERCHANT_ID")
        self.payment_link_id = os.getenv("PAYMENT_LINK_ID")
        self.payment_order_id = os.getenv("PAYMENT_ORDER_ID")

        self.customer = {
            "email": "some.email@domain.com",
            "first_name": "James",
            "last_name": "Smith",
            "phone": "0700000000"
        }
        self.items = [
            {
                "description": "Hawaii Pizza",
                "merchant_id": self.merchant_id,
                "price": 7000,
                "quantity": 2,
                "vat": 12
            }
        ]
        self.supplier = {
            "city": "Örebro",
            "name": "name",
            "organization_number": "5555555555",
            "website": "https://somewebsite.com",
            "zip": "45133"
        }
        self.swish_parameters = [
            {
                "method": "e_commerce",
                "parameters": {
                    "swish_message": "Pizza from the pizzeria"
                },
                "provider": "swish"
            }
        ]
        self.complete_create_body = {
            "customer": self.customer,
            "items": self.items,
            "locale": "sv-SE",
            "payment_order_id": self.payment_order_id,
            "payment_provider_methods": self.swish_parameters,
            "supplier": self.supplier,
            "currency": "SEK",
            "total_amount": 14000
        }
