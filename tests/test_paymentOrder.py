
from ping.payments_api import PaymentsApi
import unittest

class TestPaymentOrder(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.payments_api = PaymentsApi("a2a4f648-a50b-42fb-bda8-00c6e2f295ea")
        cls.payment_order_id ="bd3e750f-2213-45c5-9d02-0dbeb2178675"

    def test_get(self):
        
        date_from = "2019-10-12"
        date_to = "2020-10-12"

        self.assertEqual(
            self.payments_api.paymentOrder.get_payments_orders(date_from, date_to).status_code, 
            200
        )
        self.assertEqual(
            self.payments_api.paymentOrder.get_payments_orders().status_code, 
            200
        )

    def test_create(self):
        split_tree_id = "4f3a07d4-ef83-4040-bcc4-0a6e6bfab6ab"

        self.assertEqual(
            self.payments_api.paymentOrder.create_payment_order(split_tree_id).status_code, 
            200
        )

    def test_get_specific(self):
        self.assertEqual(
            self.payments_api.paymentOrder.get_payment_order(self.payment_order_id).status_code, 
            200
        )

    def test_update(self):
      pass

    def test_close(self):    
        self.assertEqual(
            self.payments_api.paymentOrder.close_payment_order(self.payment_order_id).status_code, 
            204
        )

    def test_settle(self): 
        self.assertEqual(
            self.payments_api.paymentOrder.settle_payment_order(self.payment_order_id).status_code, 
            204
        )

    def test_split(self):    
        self.assertEqual(
            self.payments_api.paymentOrder.split_payment_order(self.payment_order_id).status_code, 
            204
        )

if __name__ == '__main__':
    unittest.main()
