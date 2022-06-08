---
title: "Payments API"
excerpt: "A general description of the PaymentApi class"
---

# Ping Payments API Class Documentation

## The PaymentsApi Class

The `PaymentsApi` class acts as a factory for the Ping Payments API resource endpoints and holds the configuration of the Ping Payments API.

| Parameter     | Type     | Description                                                               |
| ------------- | -------- | ------------------------------------------------------------------------- |
| `tenant_id`   | `string` | ID given to a tenant by Ping Payments                                     |
| `environment` | `string` | API environment <br><br>Default: `production` <br><br>Optional: `sandbox` |

Using an endpoint in the PaymentsApi class:

-   Create a PaymentsApi object with a `tenant_id`.
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`.
-   Use an appropriate endpoint through the PaymentsApi object, for example: `payments_api.merchant`.

Initializing the Ping Payments API:

```python
from ping.payments_api import PaymentsApi

payments_api = PaymentsApi(
  tenant_id = '55555555-5555-5555-5555-555555555555',
  environment = 'sandbox'
)
```

## Calls to the Ping Payments API

Example using the merchant resource:

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

## API Resources

| Name          | Description                                                         |
| ------------- | ------------------------------------------------------------------- |
| merchant      | Gets all merchant functions from the `merchants.py` module          |
| payment_order | Gets all payment order functions from the `paymentOrders.py` module |
| payment       | Gets all payment functions from the `payments.py` module            |
| payout        | Gets all Payout functions from the `payouts.py` module              |
