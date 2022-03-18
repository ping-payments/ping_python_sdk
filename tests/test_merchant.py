from ping.payments_api import PaymentsApi
import unittest
from test_helper import testHelper
import uuid

class TestMerchant(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.payments_api = PaymentsApi("a2a4f648-a50b-42fb-bda8-00c6e2f295ea")
        cls.test_helper = testHelper

# Get Merchants Tests
    # gets merchants successfully
    def test_get_merchants_200(self):
        response = self.payments_api.merchant.get_merchants()
        self.test_helper.run_tests(self, response)

# Create New Merchant Tests
    # creates a merchant correctly (status code 200)
    def test_create_new_merchant_200(self):
        response = self.payments_api.merchant.create_new_merchant(
            {
                "name": "Tomten",
                "organization": {
                    "country": "SE",
                    "se_organization_number": "555555-5555"
                }
            }
        )
        self.test_helper.run_tests(self, response)
    
    # creates a merchant with incorrect values inside merchant object (status code 422)
    def test_create_new_merchant_422(self):
        response = self.payments_api.merchant.create_new_merchant(
            {
                "name": 0,
                "organization": {
                    "country": "SE",
                    "se_organization_number": "555555-5555"
                }
            }
        )
        self.test_helper.run_tests(self, response, 422)

# Get Specific Merchant Tests
    # get a specific merchant correctly (status code 200)
    def test_get_specific_merchant_200(self):
        response = self.payments_api.merchant.get_specific_merchant("612f2128-e26f-4cb1-80b6-2895af31f8b4")
        self.test_helper.run_tests(self, response)

    # get a specific merchant with wrong id format (status code 422)
    def test_get_specific_merchant_422(self):
        response = self.payments_api.merchant.get_specific_merchant(0)
        self.test_helper.run_tests(self, response, 422)
    
    # get a specific merchant with a non-existing id (status code 404)
    def test_get_specific_merchant_404(self):
        response = self.payments_api.merchant.get_specific_merchant(uuid.uuid4())
        self.test_helper.run_tests(self, response, 404)


if __name__ == '__main__':
    unittest.main()
