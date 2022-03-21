from ping.payments_api import PaymentsApi
import unittest
from test_helper import testHelper


class TestPayment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_helper = testHelper
        cls.payment_order_id = "8a6a4586-e082-49fe-b408-b92e9dc746ec"
        cls.payments_api = PaymentsApi(
            tenant_id="a2a4f648-a50b-42fb-bda8-00c6e2f295ea"
        )

    def setUp(self):
        self.dummy_body = {
            "currency": "SEK",
            "metadata": {
                "delivery_id": "368745"
                },
            "method": "dummy",
            "total_amount": 9400,
            "order_items": [
                {
                    "amount": 2500,
                    "merchant_id": "70166bfa-2b5f-42f8-abe1-a614e32ad1b2",
                    "name": "Delivery, Marios Pasta (Pasta La Vista)",
                    "vat_rate": 12
                },
                {
                    "amount": 6900,
                    "merchant_id": "70166bfa-2b5f-42f8-abe1-a614e32ad1b2",
                    "name": "Marios Pasta (Pasta La Vista)",
                    "vat_rate": 12
                }
            ],
            "provider": "dummy",
            "provider_method_parameters": {
                "desired_payment_status": "COMPLETED"
            },
            "status_callback_url": "https://somesite.com/callback"
        }

# Get Payments Tests
    # gets payment correctly
    def test_get_payment_200(self):
        payment_id = "c498dba8-bf28-4252-a16a-7c6192c05bc9"

        response = self.payments_api.payment.get_payment(self.payment_order_id, payment_id)
        self.test_helper.run_tests(self, response, 500)

    # gets payment with an incorrect id
    def test_get_payment_404(self):
        payment_id = ""

        response = self.payments_api.payment.get_payment(self.payment_order_id, payment_id)
        self.test_helper.run_tests(self, response, 404)

# Initiate Payment Tests
    # Initiate a correct payment (status code 200)
    def test_initiate_payment_200(self):
        response = self.payments_api.payment.initiate_payment(self.dummy_body, self.payment_order_id)
        self.test_helper.run_tests(self, response)

    # Initiate a payment with incorrect values inside payment object (status code 422)
    def test_initiate_payment_422(self):
        payment_order_id = "8a6a4586-e082-49fe-b408-b92e9dc746ec"
        self.dummy_body["method"] = 0

        response = self.payments_api.payment.initiate_payment(self.dummy_body, payment_order_id)
        self.test_helper.run_tests(self, response, 422)

    # Initiate a payment on a non-exisiting payment order (status code 404)
    def test_initiate_payment_404(self):
        error_payment_order_id = ""

        response = self.payments_api.payment.initiate_payment(self.dummy_body, error_payment_order_id)
        self.test_helper.run_tests(self, response, 404)


if __name__ == '__main__':
    unittest.main()
