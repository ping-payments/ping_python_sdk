from ping.payments_api import PaymentsApi
import unittest


class TestPayment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        tenant_id = "a2a4f648-a50b-42fb-bda8-00c6e2f295ea"
        cls.payments_api = PaymentsApi(tenant_id)

    def test_get_payment(self):
        payment_order_id = "8a6a4586-e082-49fe-b408-b92e9dc746ec"
        payment_id = "c498dba8-bf28-4252-a16a-7c6192c05bc9"

        response = self.payments_api.payment.get_payment(payment_order_id, payment_id)
        self.run_tests(response)

    def test_initiate_payment(self):

        payment_order_id = "8a6a4586-e082-49fe-b408-b92e9dc746ec"
        dummy_body = {
             "currency": "SEK",
             "merchant_amounts": {
                 "075b5c3c-3f17-435d-ab84-0bc57d8e67d4": 9400,
                 },
             "metadata": {
                 "delivery_id": "368745"
                 },
             "method": "dummy",
             "order_items": [
                 {
                     "amount": 2500,
                     "name": "Delivery, Marios Pasta (Pasta La Vista)",
                     "vat_rate": 12
                 },
                 {
                     "amount": 6900,
                     "name": "Marios Pasta (Pasta La Vista)",
                     "vat_rate": 12
                 }
             ],
             "provider": "dummy",
             "provider_method_parameters": {},
             "status_callback_url": "https://somesite.com/callback"
        }

        response = self.payments_api.payment.initiate_payment(dummy_body, payment_order_id)
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
