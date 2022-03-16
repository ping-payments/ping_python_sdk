from ping.payments_api import PaymentsApi
import unittest

class TestMerchant(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.payments_api = PaymentsApi("a2a4f648-a50b-42fb-bda8-00c6e2f295ea")

    def test_get(self):
        pass

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
