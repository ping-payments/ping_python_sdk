from ping.payments_api import PaymentsApi
import unittest

class TestMerchant(unittest.TestCase):
    
    def setUp(self):
        self.payments_api = PaymentsApi("a2a4f648-a50b-42fb-bda8-00c6e2f295ea")