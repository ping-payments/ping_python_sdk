from ping.configuration import get_base_url
from ping.api_resources import merchants
from ping.api_resources import paymentOrders
from ping.api_resources import payments

class Tenant():
  
  def __init__(
              self, 
              tenant_id='',
              environment='sandbox'):
  
    self.tenant_id = tenant_id
    self.base_url = get_base_url(environment)
    self.headers = {
            "Accept": "application/json",
            "tenant_id": tenant_id
        }
  
  def get_merchants(self):
    return merchants.get_merchant(self.headers, self.base_url)
  
  def create_new_merchant(self, obj):
    return merchants.create_new_merchant(self.headers, self.base_url, obj)
  
  def get_specific_merchant(self,  merchant_id):
    return merchants.get_specific_merchant(self.headers, self.base_url, merchant_id)

  def payments_orders(self):
    return paymentOrders.PaymentOrders(self.headers, self.base_url)
  
  def payments(self):
    return payments.Payments(self.headers, self.base_url)
