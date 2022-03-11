import ping 

pingPay = ping.payments_api("a2a4f648-a50b-42fb-bda8-00c6e2f295ea")
m = pingPay.merchant.get_merchants()





"""from api.payments_api.payments_api import Tenant

tenant_id="a2a4f648-a50b-42fb-bda8-00c6e2f295ea"
tenant =Tenant(tenant_id=tenant_id)
tenant2 =Tenant(tenant_id="")

list_of_merchant = tenant.Merchant.get_merchants()
list_of_merchant2 = tenant2.merchant.get_merchants()

print(list_of_merchant.status_code)
print(list_of_merchant2.status_code)"""