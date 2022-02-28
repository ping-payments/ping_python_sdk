from ping.api_resources.merchants import Merchants
from ping.api_resources.paymentOrders import PaymentOrders
from ping.api_resources.payments import Payments

class Tenant():
  
  def __init__(self, tenant_id):
    self.tenant_id = tenant_id
    
  def merchants(self):
    return Merchants(self.tenant_id)
  
  def payments_orders(self):
    return PaymentOrders(self.tenant_id)
  
  def payments(self):
    return Payments(self.tenant_id)
