import unittest
import uuid
import os
from dotenv import load_dotenv
from ping.payment_links_api import PaymentLinksApi
from tests.test_helper import TestHelper


class TestPaymentLinks(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.test_helper = TestHelper
        cls.payment_links_api = PaymentLinksApi(os.getenv("TENANT_ID"))
        cls.payment_link_id = os.getenv("PAYMENT_LINK_ID")
        cls.payment_order_id = os.getenv("PAYMENT_ORDER_ID")
        cls.merchant_id = os.getenv("MERCHANT_ID")

        cls.customer = {
            "email": "some.email@domain.com",
            "first_name": "Bertil",
            "last_name": "Jönsson",
            "phone": "0700000000"
        }
        cls.items = [
            {
                "description": "Hawaii Pizza",
                "merchant_id": cls.merchant_id,
                "price": 7000,
                "quantity": 2,
                "vat": 12
            }
        ]
        cls.supplier = {
            "city": "Örebro",
            "name": "name",
            "organization_number": "5555555555",
            "website": "https://somewebsite.com",
            "zip": "45133"
        }
        cls.swish_parameters = [
            {
                "method": "e_commerce",
                "parameters": {
                    "swish_message": "Tack för din betalning"
                },
                "provider": "swish"
            }
        ]
        cls.complete_create_body = {
            "customer": cls.customer,
            "items": cls.items,
            "locale": "sv-SE",
            "payment_order_id": cls.payment_order_id,
            "payment_provider_methods": cls.swish_parameters,
            "supplier": cls.supplier,
            "currency": "SEK",
            "total_amount": 14000
        }


# List Payment Links
    # lists all payment links correctly(status code 200)


    def test_list_payment_links_200(self):
        response = self.payment_links_api.payment_link.list()
        self.test_helper.run_tests(self, response, 200)


# Get Payment Link Tests
    # gets a payment link correctly


    def test_get_payment_link_200(self):
        response = self.payment_links_api.payment_link.get(self.payment_link_id)
        self.test_helper.run_tests(self, response, 200)

    # error - gets a payment link with an incorrect id
    def test_get_payment_link_404(self):
        payment_link_id = uuid.uuid4()

        response = self.payment_links_api.payment_link.get(payment_link_id)
        self.test_helper.run_tests(self, response, 404)

# Create Payment Link
    # Creates a payment link correctly (status code 200)
    def test_create_payment_link_200(self):
        request = self.complete_create_body
        response = self.payment_links_api.payment_link.create(request)
        self.test_helper.run_tests(self, response)

    def test_create_payment_link_non_matching_total_amount_422(self):
        request = {
            "customer": self.customer,
            "items": self.items,
            "locale": "sv-SE",
            "payment_order_id": self.payment_order_id,
            "payment_provider_methods": self.swish_parameters,
            "supplier": self.supplier,
            "currency": "SEK",
            "total_amount": 0
        }
        response = self.payment_links_api.payment_link.create(request)
        self.test_helper.run_tests(self, response, 403)

    def test_create_payment_link_no_customer_422(self):
        request = {
            "items": self.items,
            "locale": "sv-SE",
            "payment_order_id": self.payment_order_id,
            "payment_provider_methods": self.swish_parameters,
            "supplier": self.supplier,
            "currency": "SEK",
            "total_amount": 14000
        }
        response = self.payment_links_api.payment_link.create(request)
        self.test_helper.run_tests(self, response, 422)

    def test_create_payment_link_no_items(self):
        request = {
            "customer": self.customer,
            "locale": "sv-SE",
            "payment_order_id": self.payment_order_id,
            "payment_provider_methods": self.swish_parameters,
            "supplier": self.supplier,
            "currency": "SEK",
            "total_amount": 0
        }
        response = self.payment_links_api.payment_link.create(request)
        self.test_helper.run_tests(self, response, 422)

    def test_create_payment_link_no_locale(self):
        request = {
            "customer": self.customer,
            "items": self.items,
            "payment_order_id": self.payment_order_id,
            "payment_provider_methods": self.swish_parameters,
            "supplier": self.supplier,
            "currency": "SEK",
            "total_amount": 14000
        }
        response = self.payment_links_api.payment_link.create(request)
        self.test_helper.run_tests(self, response, 422)

    def test_create_payment_link_no_id_422(self):
        request = {
            "customer": self.customer,
            "items": self.items,
            "locale": "sv-SE",
            "payment_provider_methods": self.swish_parameters,
            "supplier": self.supplier,
            "currency": "SEK",
            "total_amount": 14000
        }
        response = self.payment_links_api.payment_link.create(request)
        self.test_helper.run_tests(self, response, 422)

    def test_create_payment_link_id_not_found_403(self):
        request = {
            "customer": self.customer,
            "items": self.items,
            "locale": "sv-SE",
            "payment_order_id": str(uuid.uuid4()),
            "payment_provider_methods": self.swish_parameters,
            "supplier": self.supplier,
            "currency": "SEK",
            "total_amount": 14000
        }
        response = self.payment_links_api.payment_link.create(request)
        self.test_helper.run_tests(self, response, 403)

    def test_create_payment_link_no_provider_method_parameters_422(self):
        request = {
            "customer": self.customer,
            "items": self.items,
            "locale": "sv-SE",
            "payment_order_id": self.payment_order_id,
            "supplier": self.supplier,
            "currency": "SEK",
            "total_amount": 14000
        }
        response = self.payment_links_api.payment_link.create(request)
        self.test_helper.run_tests(self, response, 422)

    def test_create_payment_link_no_supplier_422(self):
        request = {
            "customer": self.customer,
            "items": self.items,
            "locale": "sv-SE",
            "payment_order_id": self.payment_order_id,
            "payment_provider_methods": self.swish_parameters,
            "currency": "SEK",
            "total_amount": 14000
        }
        response = self.payment_links_api.payment_link.create(request)
        self.test_helper.run_tests(self, response, 422)

    def test_create_payment_link_no_currency_422(self):
        request = {
            "customer": self.customer,
            "items": self.items,
            "locale": "sv-SE",
            "payment_order_id": self.payment_order_id,
            "payment_provider_methods": self.swish_parameters,
            "supplier": self.supplier,
            "total_amount": 14000
        }
        response = self.payment_links_api.payment_link.create(request)
        self.test_helper.run_tests(self, response, 422)

    def test_cancel_payment_link_204(self):
        payment_link = self.payment_links_api.payment_link.create(self.complete_create_body)
        payment_link_id = payment_link.body["id"]
        response = self.payment_links_api.payment_link.cancel(payment_link_id)
        self.test_helper.run_tests(self, response, 204)

    def test_cancel_payment_link_id_not_found_404(self):
        response = self.payment_links_api.payment_link.cancel(uuid.uuid4())
        self.test_helper.run_tests(self, response, 404)

    def test_cancel_payment_link_already_canceled_403(self):
        response = self.payment_links_api.payment_link.cancel(self.payment_link_id)
        self.test_helper.run_tests(self, response, 403)

    def test_send_payment_link_with_sms_204(self):
        request = {
            "methods": ["sms"],
            "customer_phone": "0701231212",
        }
        response = self.payment_links_api.payment_link.send(self.payment_link_id, request)
        self.test_helper.run_tests(self, response, 204)

    def test_send_payment_link_with_email_204(self):
        request = {
            "methods": ["email"],
            "customer_email": "somemail@mail.com",
        }
        response = self.payment_links_api.payment_link.send(self.payment_link_id, request)
        self.test_helper.run_tests(self, response, 204)

    def test_send_payment_link_with_sms_and_email_204(self):
        request = {
            "methods": ["sms", "email"],
            "customer_phone": "0701231212",
            "customer_email": "somemail@mail.com"
        }
        response = self.payment_links_api.payment_link.send(self.payment_link_id, request)
        self.test_helper.run_tests(self, response, 204)

    def test_send_payment_link_with_empty_request_422(self):
        response = self.payment_links_api.payment_link.send(self.payment_link_id, {})
        self.test_helper.run_tests(self, response, 422)

    def test_send_payment_link_id_not_found_404(self):
        response = self.payment_links_api.payment_link.send(uuid.uuid4(), {"methods": ["sms"]})
        self.test_helper.run_tests(self, response, 404)


if __name__ == '__main__':
    unittest.main()
