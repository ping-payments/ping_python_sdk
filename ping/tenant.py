from ping.api_resources.merchants import Merchants
from ping.api_resources.paymentOrders import PaymentOrders
from ping.api_resources.payments import Payments

"""
merchant_id: df5e30b0-dd8d-44f0-b200-a734a55ce6e6
"""


class Tenant():
  def __init__(self, tenant_id):
    self.tenant_id = tenant_id
  def merchants(self):
    return Merchants(self.tenant_id)
  
  def payments_orders(self):
    return PaymentOrders(self.tenant_id)
  
  def payments(self):
    return Payments(self.tenant_id)


    

"""tenantId = "a2a4f648-a50b-42fb-bda8-00c6e2f295ea"

body = {
            "name": "Orange inc",
            "organization_number": "5154355555"
        }
        

tenant_object = Tenant("a2a4f648-a50b-42fb-bda8-00c6e2f295ea")

Merchants = tenant_object.merchants()
response = Merchants.get_merchants()
print(response.json())"""

