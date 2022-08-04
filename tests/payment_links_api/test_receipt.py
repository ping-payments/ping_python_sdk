import unittest
import uuid
import os
from dotenv import load_dotenv
from ping.payment_links_api import PaymentLinksApi
from tests.test_helper import testHelper

class TestReceipt(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.test_helper = testHelper
        cls.payment_links_api = PaymentLinksApi(os.getenv("PL_TENANT_ID"))    

# Get Receipt
    # get an receipt correctly(status code 200)
    def test_get_receipt_200(self):

        response = self.payment_links_api.invoice.get(os.getenv("PAYMENT_LINK_ID"))
        self.test_helper.run_tests(self, response)

    # error - gets an receipt with an incorrect id
    def test_get_receipt_id_not_found_404(self):

        response = self.payment_links_api.invoice.get(uuid.uuid4())
        self.test_helper.run_tests(self, response, 404)
    
    # error - gets a receipt with an unfinished payment link
    def test_get_receipt_not_completed_403(self):

        response = self.payment_links_api.invoice.get(os.getenv("PAYMENT_LINK_ID_NOT_COMPLETED"))
        self.test_helper.run_tests(self, response, 403)


if __name__ == '__main__':
    unittest.main()
