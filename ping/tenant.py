from api.merchants import Merchants

class Tenant():
  def __init__(self):
    self.tenant_id = ''

  def merchants(self):
    return Merchants()

t = Tenant()

Merchants = t.merchants()
print(Merchants.get_merchants())
