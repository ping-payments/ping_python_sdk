import unittest
import uuid
import os
from dotenv import load_dotenv
from ping.payment_links_api import PaymentLinksApi
from tests.test_helper import testHelper


# @unittest.skipUnless(testHelper.api_is_connected(), "A connection to the API is needed")
class TestPayment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.test_helper = testHelper
        cls.payment_link_id = os.getenv("PAYMENT_LINK_ID")
        cls.payment_links_api = PaymentLinksApi(os.getenv("TENANT_ID"))

# List Payment Links
    # lists all payment links correctly(status code 200)
    def test_list_payment_links_200(self):

        response = self.payment_links_api.payment_links.list()
        self.test_helper.run_tests(self, response, 200)


# Get Payment Link Tests
    # gets a payment link correctly
    def test_get_payment_link_200(self):

        response = self.payment_links_api.payment_links.get(self.payment_link_id)
        self.test_helper.run_tests(self, response, 200)

    # error - gets a payment link with an incorrect id
    def test_get_payment_link_404(self):
        payment_link_id = uuid.uuid4()

        response = self.payment_links_api.payment_links.get(payment_link_id)
        self.test_helper.run_tests(self, response, 404)

# Create Payment Link
    # Creates a payment link correctly (status code 200)
    def test_create_payment_link_200(self):
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
        response = self.payment_links_api.payment_links.create(request)
        self.test_helper.run_tests(self, response)

    

if __name__ == '__main__':
    unittest.main()
