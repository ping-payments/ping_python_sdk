
from ping.payments_api import PaymentsApi
import unittest

class TestPaymentOrder(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.payments_api = PaymentsApi("a2a4f648-a50b-42fb-bda8-00c6e2f295ea")

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
        pass

    def test_get_specific(self):
        pass

    def test_update(self):
        pass

    def test_close(self):
        pass

    def test_settle(self):
        pass

    def test_split(self):
        pass

if __name__ == '__main__':
    unittest.main()
