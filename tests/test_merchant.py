from ping.payments_api import PaymentsApi
import unittest



class TestMerchant(unittest.TestCase):
    
    def setUp(self):
        self.payments_api = PaymentsApi("a2a4f648-a50b-42fb-bda8-00c6e2f295ea")

    def test_get(self):
        self.assertEqual(
            self.payments_api.merchant.get_merchants().status_code, 
            200
            )

    def test_create(self):
        body = {
            "name": "Tomten",
            "organization": {
                "country": "SE",
                "se_organization_number": "555555-5555"
            }
        }
        self.assertEqual(
            self.payments_api.merchant.create_new_merchant(body).status_code, 
            200
            )

    def test_get_specific(self):
        id = "612f2128-e26f-4cb1-80b6-2895af31f8b4"
        self.assertEqual(
            self.payments_api.merchant.get_specific_merchant(id).status_code, 
            200
            )


if __name__ == '__main__':
    unittest.main()