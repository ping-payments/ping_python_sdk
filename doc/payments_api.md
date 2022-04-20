# Payments API Class Documentation

| Parameter     | Type     | Description                                                                   |
| ------------- | -------- | ----------------------------------------------------------------------------- |
| `tenant_id`   | `string` | The ID given to the tenant by Ping Payments                                   |
| `environment` | `string` | The API environment <br><br>Default: `production` <br><br>Optional: `sandbox` |

The Payments API can be initialized as follows:

```python
from ping.payments_api import PaymentsApi

payments_api = PaymentsApi(
  tenant_id = '55555555-5555-5555-5555-555555555555',
  environment = 'sandbox'
)
```

## Make Calls to the Payments API

```python
from ping.payments_api import PaymentsApi

payments_api = PaymentsApi(
  tenant_id = '55555555-5555-5555-5555-555555555555',
  environment = 'sandbox'
)

result = payments_api.merchant.get_merchants()
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

## Ping Payments API

This class acts as a factory for the Payments APIs resources and hold the configuration of that API.

## API Resources

| Name          | Description                                                          |
| ------------- | -------------------------------------------------------------------- |
| merchant      | Gets all merchant endpoints from the `merchants.py` module           |
| payment_order | Gets all Payment Order endpoints from the `payment_orders.py` module |
| payment       | Gets all Payment endpoints from the `payments.py` module             |
| payout        | Gets all Payout endpoints from the `payouts.py` module               |
