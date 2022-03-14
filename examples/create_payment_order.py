from ping.payments_api import PaymentsApi

tenant_id = "a2a4f648-a50b-42fb-bda8-00c6e2f295ea"
payments_api = PaymentsApi(tenant_id)

split_tree_id = "25313ee5-a7ad-4a0c-8190-c3d492add8d3"

payment_order_id = "de4fbdde-a1df-40a1-942c-c26c70d837ee"

result = payments_api.paymentOrder.update_payment_order(payment_order_id, "4f3a07d4-ef83-4040-bcc4-0a6e6bfab6ab")
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
    print(result.status_code)
    print("error")
