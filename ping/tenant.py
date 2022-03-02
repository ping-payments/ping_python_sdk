from ping.configuration import get_base_url
from ping.api_resources.merchants import get_merchants
from ping.api_resources.merchants import create_new_merchants
from ping.api_resources.merchants import get_specific_merchant
from ping.api_resources.paymentOrders import PaymentOrders
from ping.api_resources.payments import Payments

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
    return get_merchants(self.headers, self.base_url)
  
  def create_new_merchants(self, obj):
    return create_new_merchants(self.headers, self.base_url, obj)
  
  def get_specific_merchants(self,  merchant_id):
    return get_specific_merchant(self.headers, self.base_url, merchant_id)

  def payments_orders(self):
    return PaymentOrders(self.headers, self.base_url)
  
  def payments(self):
    return Payments(self.headers, self.base_url)
