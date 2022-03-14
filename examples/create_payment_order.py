from ping.payments_api import PaymentsApi

tenant_id = "a2a4f648-a50b-42fb-bda8-00c6e2f295ea"
payments_api = PaymentsApi(tenant_id)

split_tree_id = "25313ee5-a7ad-4a0c-8190-c3d492add8d3"

payment_order_id = "03c0b995-fab1-4cb7-b179-3ef25aa9172a"

result = payments_api.paymentOrder.close_payment_order(payment_order_id)

if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
    print(result.status_code)
    print("error")
