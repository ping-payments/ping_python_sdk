from ping.api_resources import merchants
from ping.api_resources import paymentOrders
from ping.api_resources import payments
from ping.configuration import get_base_url

class Tenant:
  def __init__(self, tenant_id="", environment="sandbox"):
    self.data = {
      "base_url": get_base_url(environment),
      "headers": {
        "Accept": "application/json",
        "tenant_id": tenant_id
      }
    }
    self.read_only()
    
   
  def read_only(self):
    self.Merchant = self.Merchant(self.data)
    self.PaymentOrder = self.PaymentOrder(self.data)
    self.Payment = self.Payment(self.data)

  class Merchant():
    def __init__(self, data):
        self.data = data

    def get_merchants(self):
      return merchants.get_merchants(self.data["headers"], self.data["base_url"])

    def create_new_merchant(self, obj):
          return merchants.create_new_merchant(self.data["headers"], self.data["base_url"], obj)

    def get_specific_merchant(self, merchant_id):
        return merchants.get_specific_merchant(self.data["headers"], self.data["base_url"], merchant_id)

    #Payment Order endpoints
  class PaymentOrder():
    def __init__(self, data):
        self.data = data

    def payments_orders(self):
      return paymentOrders.PaymentOrders(self.data["headers"], self.data["base_url"])

    #Payment endpoints
  class Payment():
    def __init__(self, data):
        self.data = data

    def initiate_payment(self, obj, payment_order_id):
      return payments.initiate_payment(self.data["headers"], self.data["base_url"], obj, payment_order_id)

    def get_payment(self, payment_order_id, payment_id):
      return payments.get_payment(self.data["headers"], self.data["base_url"], payment_order_id, payment_id)
