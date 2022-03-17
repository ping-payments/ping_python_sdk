from ping.payments_api import PaymentsApi
import unittest


class TestMerchant(unittest.TestCase):

    @classmethod
    def setUpClass(clf):
        clf.payments_api = PaymentsApi("a2a4f648-a50b-42fb-bda8-00c6e2f295ea")

    def test_get_merchants(self):
        response = self.payments_api.merchant.get_merchants()
        self.run_tests(response)

    def test_create_new_merchant(self):
        response = self.payments_api.merchant.create_new_merchant(
            {
                "name": "Tomten",
                "organization": {
                    "country": "SE",
                    "se_organization_number": "555555-5555"
                }
            }
        )
        self.run_tests(response)

    def test_get_specific_merchant(self):
        response = self.payments_api.merchant.get_specific_merchant("612f2128-e26f-4cb1-80b6-2895af31f8b4")
        self.run_tests(response)

    def run_tests(self, response):
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.is_error())
        self.assertTrue(response.is_success())
        self.assertIsNotNone(response.body)
        self.assertIsNone(response.errors)


if __name__ == '__main__':
    unittest.main()
