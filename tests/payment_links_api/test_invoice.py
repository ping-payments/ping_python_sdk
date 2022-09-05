import unittest
import uuid
import os
from dotenv import load_dotenv
from ping.payment_links_api import PaymentLinksApi
from tests.test_helper import testHelper

class TestInvoice(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.test_helper = testHelper
        cls.payment_link_id = os.getenv("PAYMENT_LINK_ID")
        cls.payment_links_api = PaymentLinksApi(os.getenv("PL_TENANT_ID"))    

        cls.customer = {
            "email": "some.email@domain.com",
            "first_name": "Bertil",
            "last_name": "Jönsson",
            "phone": "0700000000"
        }
        cls.items =[
            {
                "description": "Hawaii Pizza",
                "merchant_id": os.getenv("PL_MERCHANT_ID"),
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
            "payment_order_id": os.getenv("PL_ORDER_ID"),
            "payment_provider_methods": cls.swish_parameters,
            "supplier": cls.supplier,
            "currency": "SEK",
            "total_amount": 14000
        }

# Get Invoice
    # get an invoice correctly(status code 200)
    def test_get_invoice_200(self):

        response = self.payment_links_api.invoice.get(self.payment_link_id)
        self.test_helper.run_tests(self, response)

    # error - gets an invoice with an incorrect id
    def test_get_invoice_id_not_found_404(self):

        payment_link_id = uuid.uuid4()
        response = self.payment_links_api.invoice.get(payment_link_id)
        self.test_helper.run_tests(self, response, 404)
    
    # error - gets a non existing invoice
    def test_get_invoice_no_exisiting_invoice_403(self):

        response = self.payment_links_api.invoice.get(os.getenv("PAYMENT_LINK_ID_NO_INVOICE"))
        self.test_helper.run_tests(self, response, 403)


# Create an invoice
    # Creates an invoice correctly (status code 200)
    def test_create_invoice_with_OCR_200(self):
        payment_link = self.payment_links_api.payment_link.create(self.complete_create_body)
        payment_link_id = payment_link.body["id"]
        response = self.payment_links_api.invoice.create(payment_link_id, {"reference_type": "OCR"})
        self.test_helper.run_tests(self, response, 204)


if __name__ == '__main__':
    unittest.main()
