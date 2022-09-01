import os
import unittest
import uuid
from dotenv import load_dotenv
from ping.payments_api import PaymentsApi
from tests.test_helper import testHelper

@unittest.skipUnless(testHelper.api_is_connected(), "A connection to the API is needed")
class TestPayout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        load_dotenv()

        cls.payments_api = PaymentsApi(os.getenv("TENANT_ID"))
        cls.test_helper = testHelper

# Get Payout Tests
    # get a list of payouts correctly (status code 200)
    def test_list_200(self): 
    
        response_date = self.payments_api.payout.list("2020-03-27T09:42:30Z", "2022-03-27T09:42:30Z")
        response = self.payments_api.payout.list()

        # tests with start-end date
        self.test_helper.run_tests(self, response_date)

        # tests without date
        self.test_helper.run_tests(self, response)

    # get payouts with impossible dates (status code 422)
    def test_list_422(self):
        response_date = self.payments_api.payout.list("12/90/2019", "40/10/2020")
        self.test_helper.run_tests(self, response_date, 422)

# Get Payout Tests
    # gets a payout correctly (status code 200)
    def test_get_200(self):
        response = self.payments_api.payout.get(os.getenv("PAYOUT_ID"))
        self.test_helper.run_tests(self, response)
    
    # get a payout with incorrect id format (status code 422)
    def test_get_422(self):
        response = self.payments_api.payout.get(0)
        self.test_helper.run_tests(self, response, 422)
    
    # get a payout with a non-existing id (status code 404)
    def test_get_404(self):
        response = self.payments_api.payout.get(uuid.uuid4())
        self.test_helper.run_tests(self, response, 404)


if __name__ == '__main__':
    unittest.main()
