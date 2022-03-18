from ping.payments_api import PaymentsApi
import unittest
from test_helper import testHelper

class TestPaymentOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.payments_api = PaymentsApi("a2a4f648-a50b-42fb-bda8-00c6e2f295ea")
        cls.payment_order_id = "bd3e750f-2213-45c5-9d02-0dbeb2178675"
        cls.split_tree_id = "4f3a07d4-ef83-4040-bcc4-0a6e6bfab6ab"
        cls.test_helper = testHelper

    def test_get_payment_orders(self):
        response_date = self.payments_api.paymentOrder.get_payments_orders("2019-10-12", "2020-10-12")
        response = self.payments_api.paymentOrder.get_payments_orders()

        # tests with start-end date
        self.run_tests(response_date)

        # tests without date
        self.run_tests(response)

    def test_create_payment_order(self):
        response = self.payments_api.paymentOrder.create_payment_order(self.split_tree_id)
        self.run_tests(response)

    def test_get_payment_order(self):
        response = self.payments_api.paymentOrder.get_payment_order(self.payment_order_id)
        self.run_tests(response)

    def test_update_payment_order(self):
        '''
        response = self.payments_api.paymentOrder.update_payment_order(
            self.payment_order_id,
            self.split_tree_id
        )
        self.run_tests(response, 204)
        '''

    def test_close_payment_order(self):
        response = self.payments_api.paymentOrder.close_payment_order(self.payment_order_id)
        self.run_tests(response, 204)

    def test_settle_payment_order(self):
        response = self.payments_api.paymentOrder.settle_payment_order(self.payment_order_id)
        self.run_tests(response, 204)

    def test_split_payment_order(self):
        response = self.payments_api.paymentOrder.split_payment_order(self.payment_order_id)
        self.run_tests(response, 204)

    def run_tests(self, response, status=200):
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, status)
        self.assertFalse(response.is_error())
        self.assertTrue(response.is_success())
        self.assertIsNotNone(response.body)
        self.assertIsNone(response.errors)


if __name__ == '__main__':
    unittest.main()
