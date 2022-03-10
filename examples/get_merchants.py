import ping

ping.set_values(tenant_id="a2a4f648-a50b-42fb-bda8-00c6e2f295ea")

list_of_merchant = ping.Merchant.get_merchants()
print(list_of_merchant.status_code)






