from ping.api_resources import merchants
from ping.api_resources import paymentOrders
from ping.api_resources import payments
from ping import values


class Merchant():
  def get_merchants():

    return merchants.get_merchants(values["headers"], values["base_url"])

  def create_new_merchant(obj):
        return merchants.create_new_merchant(values["headers"], values["base_url"], obj)
        
  def get_specific_merchant(merchant_id):
      return merchants.get_specific_merchant(values["headers"], values["base_url"], merchant_id)

  #Payment Order endpoints
class PaymentOrder():

    def payments_orders():
      return paymentOrders.PaymentOrders(values["headers"], values["base_url"])

  #Payment endpoints
class Payment():
    def initiate_payment(obj, payment_order_id):
      return payments.initiate_payment(values["headers"], values["base_url"], obj, payment_order_id)

    def get_payment( payment_order_id, payment_id):
      return payments.get_payment(values["headers"], values["base_url"], payment_order_id, payment_id)
