from ping.payments_api import PaymentsApi
import unittest


class TestPaymentOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.payments_api = PaymentsApi("a2a4f648-a50b-42fb-bda8-00c6e2f295ea")
        cls.payment_order_id = "bd3e750f-2213-45c5-9d02-0dbeb2178675"

    def test_get_payment_orders(self):
        response_date = self.payments_api.paymentOrder.get_payments_orders("2019-10-12", "2020-10-12")
        response = self.payments_api.paymentOrder.get_payments_orders()

        # tests with start-end date
        self.assertIsNotNone(response)
        self.assertEqual(response_date.status_code, 200)
        self.assertTrue(response_date.is_success())
        self.assertFalse(response_date.is_error())
        self.assertIsNotNone(response.body)

        # tests without date
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_success())
        self.assertFalse(response.is_error())
        self.assertIsNotNone(response.body)

    def test_create_payment_order(self):
        response = self.payments_api.paymentOrder.create_payment_order("4f3a07d4-ef83-4040-bcc4-0a6e6bfab6ab")

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_success())
        self.assertFalse(response.is_error())
        self.assertIsNotNone(response.body)

    def test_get_payment_order(self):
        response = self.payments_api.paymentOrder.get_payment_order(self.payment_order_id)

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_success())
        self.assertFalse(response.is_error())
        self.assertIsNotNone(response.body)

    def test_update_payment_order(self):
        pass

    def test_close_payment_order(self):
        response = self.payments_api.paymentOrder.close_payment_order(self.payment_order_id)

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 204)
        self.assertTrue(response.is_success())
        self.assertFalse(response.is_error())
        self.assertIsNotNone(response.body)

    def test_settle_payment_order(self):
        response = self.payments_api.paymentOrder.settle_payment_order(self.payment_order_id)

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 204)
        self.assertTrue(response.is_success())
        self.assertFalse(response.is_error())
        self.assertIsNotNone(response.body)

    def test_split_payment_order(self):
        response = self.payments_api.paymentOrder.split_payment_order(self.payment_order_id)

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 204)
        self.assertTrue(response.is_success())
        self.assertFalse(response.is_error())
        self.assertIsNotNone(response.body)


if __name__ == '__main__':
    unittest.main()
