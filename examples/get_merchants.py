from ping.tenant import Tenant

tenantId = "a2a4f648-a50b-42fb-bda8-00c6e2f295ea"
tenant_object = Tenant(tenantId)
merchants = tenant_object.merchants()

list_of_merchants = merchants.get_merchants()
print(list_of_merchants.text)


