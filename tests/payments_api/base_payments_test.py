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

        self.dummy_body = {
            "currency": "SEK",
            "metadata": {
                "delivery_id": "368745"
            },
            "method": "dummy",
            "order_items": [
                {
                    "amount": 2500,
                    "merchant_id": os.getenv("MERCHANT_ID"),
                    "name": "Delivery, Marios Pasta (Pasta La Vista)",
                    "vat_rate": 12
                },
            ],
            "provider": "dummy",
            "provider_method_parameters": {
                "desired_payment_status": "COMPLETED"
            },
            "total_amount": 2500
        }

    def await_payment_status(self, payment_order_id, payment_id):
        is_completed = False
        while not is_completed:
            payment = self.payments_api.payment.get(payment_order_id, payment_id)
            if payment.is_success():
                if payment.body["status"] == "COMPLETED":
                    is_completed = True
            else:
                break

    def prepare_payment_order_handling(self):

        payment_order = self.payments_api.paymentOrder.create(os.getenv("SPLIT_TREE_ID"), "SEK")
        payment_order_id = payment_order.body["id"]

        payment_response = self.payments_api.payment.initiate(self.dummy_body, payment_order_id)

        payment_id = payment_response.body["id"]

        return payment_order_id, payment_id
