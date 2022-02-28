from ping.configuration import Configuration
from ping.api_resources.merchants import Merchants
from ping.api_resources.paymentOrders import PaymentOrders
from ping.api_resources.payments import Payments

class Tenant():
  
  def __init__(self, 
              tenant_id='',
              environment='sandbox'):
    
    self.tenant_id = tenant_id
    self.base_url = Configuration(environment).get_base_url()
  
    
  def merchants(self):
    return Merchants(self.tenant_id, self.base_url)
  
  def payments_orders(self):
    return PaymentOrders(self.tenant_id, self.base_url)
  
  def payments(self):
    return Payments(self.tenant_id, self.base_url)
