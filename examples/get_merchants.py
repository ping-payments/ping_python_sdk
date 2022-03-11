from ping.payments_api import PaymentsApi

pay_api = PaymentsApi("a2a4f648-a50b-42fb-bda8-00c6e2f295ea")

result = pay_api.Merchant.get_merchants()

if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)