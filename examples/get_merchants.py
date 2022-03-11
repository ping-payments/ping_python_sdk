import ping 

p
ping_pay_api = ping.payments_api("a2a4f648-a50b-42fb-bda8-00c6e2f295ea")
result = ping_pay_api.Merchant.get_merchants()

if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)