from ping.configuration import get_base_url
from ping.api_resources import merchants
from ping.api_resources import paymentOrders
from ping.api_resources import payments

class Tenant():
  
  def __init__(
              self,
              tenant_id='',
              environment='sandbox'):
    global base_url
    global headers
    base_url = get_base_url(environment)
    headers = {
      "Accept": "application/json",
      "tenant_id": tenant_id
    }
    
  class Merchant():
  #Merchant endpoints
    def get_merchants():
      return merchants.get_merchants(headers, base_url)
    def create_new_merchant(obj):
      return merchants.create_new_merchant(headers, base_url, obj)
    def get_specific_merchant(merchant_id):
      return merchants.get_specific_merchant(headers, base_url, merchant_id)
  class PaymentOrder():
  #Payment Order endpoints
    def payments_orders():
      return paymentOrders.PaymentOrders(headers,base_url)
  class Payment():
  #Payment endpoints
    def initiate_payment(obj, payment_order_id):
      return payments.initiate_payment(headers, base_url, obj, payment_order_id)
    def get_payment( payment_order_id, payment_id):
      return payments.get_payment(headers, base_url, payment_order_id, payment_id)
