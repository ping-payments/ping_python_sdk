from ping.tenant import Tenant

tenant_id = "a2a4f648-a50b-42fb-bda8-00c6e2f295ea"
tenant = Tenant(tenant_id = tenant_id)

list_of_merchants = tenant.get_merchants()
print(list_of_merchants.text)
print(list_of_merchants.status_code)


