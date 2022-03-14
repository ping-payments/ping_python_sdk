from ping.payments_api import PaymentsApi

tenant_id = "a2a4f648-a50b-42fb-bda8-00c6e2f295ea"
payments_api = PaymentsApi(tenant_id)

split_tree_id = {
  "split_tree_id": "268b877b-a23a-4181-8309-5e2af4802ce8"
}
result = payments_api.paymentOrder.create_payment_order(split_tree_id)

if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
