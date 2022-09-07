import unittest
import os
from tests.test_helper import TestHelper
from ping.payments_api import PaymentsApi


class BasePaymentsTest(unittest.TestCase):

    def setUp(self):
        self.test_helper = TestHelper
        self.payments_api = PaymentsApi(os.getenv("TENANT_ID"))
        self.merchant_id = os.getenv("MERCHANT_ID")
        self.split_tree_id = os.getenv("SPLIT_TREE_ID")
        self.payment_id = os.getenv("PAYMENT_ID")
        self.payment_order_id = os.getenv("PAYMENT_ORDER_ID")
