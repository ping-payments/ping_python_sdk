from ping.payments_api import PaymentsApi

tenant_id = "a2a4f648-a50b-42fb-bda8-00c6e2f295ea"
payments_api = PaymentsApi(tenant_id)

result = payments_api.merchant.get_merchants()

if result.is_success():
 print(result.body)
 print("success")
elif result.is_error():
 print(result.errors)
 print("error")
