from ping.payments_api import PaymentsApi

tenant_id = "a2a4f648-a50b-42fb-bda8-00c6e2f295ea"
payments_api = PaymentsApi(tenant_id=tenant_id)

payment_order_id = "8a6a4586-e082-49fe-b408-b92e9dc746ec"
payment_object = {
  "currency": "SEK",
  "metadata": {
    "delivery_id": "368745"
  },
  "total_amount": 9400,
  "method": "dummy",
  "order_items": [
    {
      "amount": 2500,
      "merchant_id": "075b5c3c-3f17-435d-ab84-0bc57d8e67d4",
      "name": "Delivery, Marios Pasta (Pasta La Vista)",
      "vat_rate": 12
    },
    {
      "amount": 6900,
      "merchant_id": "075b5c3c-3f17-435d-ab84-0bc57d8e67d4",
      "name": "Marios Pasta (Pasta La Vista)",
      "vat_rate": 12
    }
  ],
  "provider": "dummy",
  "provider_method_parameters": {},
  "status_callback_url": "https://somesite.com/callback"
}

result = payments_api.payment.initiate_payment(payment_object, payment_order_id)

if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.status_code)
    print(result.errors)
    print("error")
