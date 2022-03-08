from ping.tenant import Tenant

tenant_id = "a2a4f648-a50b-42fb-bda8-00c6e2f295ea"
tenant = Tenant(tenant_id = tenant_id)

list_of_merchants = tenant.Merchant.get_merchants()
if list_of_merchants.is_success:
    print(list_of_merchants.body)
    print("success")
elif list_of_merchants.error():
    print(list_of_merchants.errors)

