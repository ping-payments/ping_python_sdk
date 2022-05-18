# Payment Order

```python
from ping.payments_api import PaymentsApi
payments_api = PaymentsApi(
  tenant_id = '55555555-5555-5555-5555-555555555555',
  environment = 'sandbox'
)
payments_api.paymentOrder.get_payment_orders()
payments_api.paymentOrder.create_payment_order()
payments_api.paymentOrder.get_payment_order()
payments_api.paymentOrder.update_payment_order()
payments_api.paymentOrder.close_payment_order()
payments_api.paymentOrder.split_payment_order()
payments_api.paymentOrder.settle_payment_order()
```

## Module Name

`paymentOrders`

## Functions

-   [Get Payment Orders](/doc/api_resources/payments_api//paymentOrder.md#get-payment-orders)
-   [Create New Paymkent Order](/doc/api_resources/payments_api//paymentOrder.md#create-new-payment-order)
-   [Get Specific Payment Order](/doc/api_resources/payments_api//paymentOrder.md#get-specific-payment-order)
-   [Update Payment Order](/doc/api_resources/payments_api//paymentOrder.md#update-payment-order)
-   [Close Payment Order](/doc/api_resources/payments_api//paymentOrder.md#close-payment-order)
-   [Split Payment Order](/doc/api_resources/payments_api//paymentOrder.md#split-payment-order)
-   [Settle Payment Order](/doc/api_resources/payments_api//paymentOrder.md#settle-payment-order)

# Get Payment Orders

Gets and returns an object of all the payment orders and optionally between dates

You need to create a PaymentsApi object with a `tenant_id` as a parameter to access `get_payment_orders()`. You can also send in an environment parameter if you wish to test your code towards a `sandbox` environment but the default value is `production`. This function can also take two dates as optional parameters if you wish to get all `payment_orders` between two dates. If the tenant_id exists and the optional dates are valid, the function will return an object containing a list of payment orders. Otherwise an error object is returned.

```python
def get_payment_orders(date_from=None, date_to=None)
```

The date-time parameters follow the ISO Timestamp format (e.g. 2022-03-27T09:42:30Z)

| Parameter   | Type                 | Required | Format   | Description                                       |
| ----------- | -------------------- | -------- | -------- | ------------------------------------------------- |
| `date_from` | `string($date-time)` | No       | ISO 8601 | Start date to find payment orders after that date |
| `date_to`   | `string($date-time)` | No       | ISO 8601 | End date to find payment orders before that date  |

## Response Type

```python
  result = payments_api.paymentOrder.get_payment_orders()
  print(result.status_code)
```

### 200

Successfully got payment orders. A json object containing an array of payment orders for the given tenant has been returned.

Example:

```python
[
  {
    "created_at": "2021-11-05T10:04:19.275000Z",
    "id": "55555555-5555-5555-5555-555555555555",
    "payments": [
      {
        "currency": "SEK",
        "id": "55555555-5555-5555-5555-555555555555",
        "method": "autogiro",
        "order_items": [],
        "provider": "bankgirot",
        "status": "COMPLETED"
      }
    ],
    "status": "OPEN"
  },
  {
    "created_at": "2021-11-15T09:15:01.400000Z",
    "id": "55555555-5555-5555-5555-555555555555",
    "payments": [
      {
        "currency": "SEK",
        "id": "55555555-5555-5555-5555-555555555555",
        "metadata": {},
        "method": "mobile",
        "order_items": [],
        "provider": "swish",
        "status": "ABORTED"
      }
    ],
    "status": "OPEN"
  }
]
```

### 403

API Error

Example:

```python
{
  "errors": [
    {
      "description": "This operation cannot be completed under certain conditions",
      "error": "operation_forbidden"
    }
  ]
}
```

### 422

Validation Error

Example:

```python
{
  "errors": [
    {
      "description": "null value where string expected",
      "error": "null_value",
      "property": "open_banking.success_url"
    }
  ]
}
```

## Example Usage

```python
payments_api = PaymentsApi(
  tenant_id = '55555555-5555-5555-5555-555555555555',
  environment = 'sandbox'
)

result = payments_api.paymentOrder.get_payment_order(
  date_to = "2000-03-27T09:42:30Z"
  date_from = "2022-03-27T09:42:30Z"
)

if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Create New Payment Order

Creates a new payment order connected to a split tree.

You need to create a PaymentApi object with a `tenant_id` as a parameter to access `create_payment_order()`. You can also send in an environment parameter if you wish to test your code towards a `sandbox` environment but the default value is `production`. The function itself requires a `split_tree_id` of a specific split tree and `currency` that determines what type of currency this payment order can handle, as parameters. If all parameters are correct, an object will be returned containing a `payment_order_id`. Otherwise an error object is returned.

```python
def create_payment_order(split_tree_id)
```

| Parameter       | Type     | Required | Description                                                                                                |
| --------------- | -------- | -------- | ---------------------------------------------------------------------------------------------------------- |
| `split_tree_id` | `string` | Yes      | A string containing the ID of a specific split tree                                                        |
| `currency`      | `string` | Yes      | Enum: `SEK`, `NOK` <br>Type of currency used for this payment order. A payments currency must be the same. |

## Response Type

```python
  result = payments_api.paymentOrder.create_payment_order(split_tree_id, currency)
  print(result.status_code)
```

### 200

Successfully created a payment order. A json object containing the id of the created payment order has been returned.

Example:

```python
{
  "id": "55555555-5555-5555-5555-555555555555"
}
```

### 403

API Error

Example:

```python
{
  "errors": [
    {
      "description": "This operation cannot be completed under certain conditions",
      "error": "operation_forbidden"
    }
  ]
}
```

### 422

Validation Error

Example:

```python
{
  "errors": [
    {
      "description": "null value where string expected",
      "error": "null_value",
      "property": "open_banking.success_url"
    }
  ]
}
```

## Example Usage

```python
payments_api = PaymentsApi(
  tenant_id = '55555555-5555-5555-5555-555555555555',
  environment = 'sandbox'
)
split_tree_id = "55555555-5555-5555-5555-555555555555"
currency = "SEK"

result = payemnts_api.payment_order.create_payment_order(split_tree_id, currency)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Get Specific Payment Order

Gets a specific payment order with a `payment_order_id`.

You need to create a PaymentsApi object with a `tenant_id` as a parameter to access `get_payment_order()`. You can also send in an environment parameter if you wish to test your code towards a `sandbox` environment but the default value is `production`. The function itself requires a `payment_order_id` as a parameter. If the `tenant_id` exists and has a payment order with that `payment_order_id` then an object containing that payment order will be returned. Otherwise an error object is returned.

```python
def get_payment_order(payment_order_id)
```

| Parameter          | Type     | Description                                            |
| ------------------ | -------- | ------------------------------------------------------ |
| `payment_order_id` | `string` | A string containing the ID of a specific payment order |

## Response Type

```python
  result = payments_api.paymentOrder.get_payment_order(payment_order_id)
  print(result.status_code)
```

### 200

Successfully returned a payment order. A json object containing a specific payment order with the given `payment_order_id` has been returned.

Example:

```python
{
  "created_at": "2021-11-15T09:15:01.400000Z",
  "id": "55555555-5555-5555-5555-555555555555",
  "payments": [
    {
      "currency": "SEK",
      "id": "55555555-5555-5555-5555-555555555555",
      "metadata": {},
      "method": "mobile",
      "order_items": [],
      "provider": "swish",
      "status": "COMPLETED"
    }
  ]
}
```

### 403

API Error

Example:

```python
{
  "errors": [
    {
      "description": "This operation cannot be completed under certain conditions",
      "error": "operation_forbidden"
    }
  ]
}
```

### 404

Payment Order could not be found.

The given `payment_order_id` could not be found.

### 422

Validation Error

Example:

```python
{
  "errors": [
    {
      "description": "null value where string expected",
      "error": "null_value",
      "property": "open_banking.success_url"
    }
  ]
}
```

## Example Usage

```python
payments_api = PaymentsApi(
  tenant_id = '55555555-5555-5555-5555-555555555555',
  environment = 'sandbox'
)
payment_order_id = '55555555-5555-5555-5555-555555555555'

result = payments_api.paymentOrder.get_payment_order(payment_order_id)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Update Payment Order

Updates a payment order. Used for updating which split tree to use when splitting.

You need to create a PaymentsApi object with a `tenant_id` as a parameter to access `update_payment_order()`. You can also send in an environment parameter if you wish to test your code towards a `sandbox` environment but the default value is `production`. This function can also requires a `payment_order_id` of the payment order you want to update and a new `split_tree_id` as a parameter. If the tenant_id exists and there is a split tree with the given `split_tree_id`, this function will return a successfull response. Otherwise an error object is returned.

```python
def update_payment_order(payment_order_id, split_tree_id)
```

| Parameter          | Type     | Description                                            |
| ------------------ | -------- | ------------------------------------------------------ |
| `payment_order_id` | `string` | A string containing the ID of a specific payment order |
| `split_tree_id`    | `string` | A string containing the ID of a specific split tree    |

## Response Type

```python
  result = payments_api.paymentOrder.update_payment_order(payment_order_id, split_tree_id)
  print(result.status_code)
```

### 204

The payment order was successfully updated

### 403

API Error

Example:

```python
{
  "errors": [
    {
      "description": "This operation cannot be completed under certain conditions",
      "error": "operation_forbidden"
    }
  ]
}
```

### 404

Payment order could not be found

`payment_order_id` or `split_tree_id` could not be found

### 422

Validation Error

Example:

```python
{
  "errors": [
    {
      "description": "null value where string expected",
      "error": "null_value",
      "property": "open_banking.success_url"
    }
  ]
}
```

## Example Usage

```python
payments_api = PaymentsApi(
  tenant_id = '55555555-5555-5555-5555-555555555555',
  environment = 'sandbox'
)
payment_order_id = '55555555-5555-5555-5555-555555555555'
split_tree_id = '55555555-5555-5555-5555-555555555555'

result = payments_api.paymentOrder.update_payment_order(payment_order_id, split_tree_id)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Close Payment Order

Closes a payment order for further payments

You need to create a PaymentsApi object with a `tenant_id` as a parameter to access `close_payment_order()`. You can also send in an environment parameter if you wish to test your code towards a `sandbox` environment but the default value is `production`. This function also requires a `payment_order_id` of the payment order you want to close. If the `tenant_id` exists and the given `payment_order_id` is connected to a payment order, this function will return a successfull response. Otherwise an error object is returned.

```python
def close_payment_order(payment_order_id)
```

| Parameter          | Type     | Required | Description                                            |
| ------------------ | -------- | -------- | ------------------------------------------------------ |
| `payment_order_id` | `string` | Yes      | A string containing the ID of a specific payment order |

## Response Type

```python
  result = payments_api.paymentOrder.close_payment_order(payment_order_id)
  print(result.status_code)
```

### 204

Payment order was successfully closed

### 403

API Error

Example:

```python
{
  "errors": [
    {
      "description": "This operation cannot be completed under certain conditions",
      "error": "operation_forbidden"
    }
  ]
}
```

### 404

Payment order could not be found.

`payment_order_id` does not match a payment order

### 422

Validation Error

Example:

```python
{
  "errors": [
    {
      "description": "null value where string expected",
      "error": "null_value",
      "property": "open_banking.success_url"
    }
  ]
}
```

## Example Usage

```python
payments_api = PaymentsApi(
  tenant_id = '55555555-5555-5555-5555-555555555555',
  environment = 'sandbox'
)
payment_order_id = '55555555-5555-5555-5555-555555555555'

result = payments_api.paymentOrder.close_payment_order(payment_order_id)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Split Payment Order

Executes a split of a payment order. Used when services/goods have been provided/delivered. Can still be partly refunded

You need to create a PaymentsApi object with a `tenant_id` as a parameter to access `split_payment_order()`. You can also send in an environment parameter if you wish to test your code towards a `sandbox` environment but the default value is `production`. This function also requires a `payment_order_id` of the payment order you want to split. If the `tenant_id` exists and the given `payment_order_id` is connected to a payment order, this function will return a successfull response. Otherwise an error object is returned.

```python
def split_payment_order(payment_order_id, fast_forward=False)
```

| Parameter          | Type      | Required | Description                                                                        |
| ------------------ | --------- | -------- | ---------------------------------------------------------------------------------- |
| `payment_order_id` | `string`  | Yes      | A string containing the ID of a specific payment order                             |
| `fast_forward`     | `boolean` | No       | A boolean that closes and splits a payment order when true. Dafault value is false |

## Response Type

```python
  result = payments_api.paymentOrder.split_payment_order(payment_order_id, fast_forward=False)
  print(result.status_code)
```

### 204

Payment order was successfully split

### 403

API Error

Example:

```python
{
  "errors": [
    {
      "description": "This operation cannot be completed under certain conditions",
      "error": "operation_forbidden"
    }
  ]
}
```

### 404

Payment order could not be found.

`payment_order_id` does not match a payment order

### 422

Validation Error

Example:

```python
{
  "errors": [
    {
      "description": "null value where string expected",
      "error": "null_value",
      "property": "open_banking.success_url"
    }
  ]
}
```

## Example Usage

```python
payments_api = PaymentsApi(
  tenant_id = '55555555-5555-5555-5555-555555555555',
  environment = 'sandbox'
)
payment_order_id = '55555555-5555-5555-5555-555555555555'

result = payments_api.paymentOrder.split_payment_order(payment_order_id, fast_forward=False)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Settle Payment Order

Settles a payment order for future payout. Refunds will no longer be possible.

You need to create a PaymentsApi object with a `tenant_id` as a parameter to access `settle_payment_order()`. You can also send in an environment parameter if you wish to test your code towards a `sandbox` environment but the default value is `production`. This function also requires a `payment_order_id` of the payment order you want to settle. If the `tenant_id` exists and the given `payment_order_id` is connected to a payment order, this function will return a successfull response. Otherwise an error object is returned.

```python
def settle_payment_order(payment_order_id, fast_forward=False)
```

| Parameter          | Type      | Required | Description                                                                                                                            |
| ------------------ | --------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_order_id` | `string`  | Yes      | A string containing the ID of a specific payment order                                                                                 |
| `fast_forward`     | `boolean` | No       | An object containing boolean that closes (if not already closed), splits and settles a payment order when true. Dafault value is false |

## Response Type

```python
  result = payments_api.paymentOrder.settle_payment_order(payment_order_id, fast_forward)
  print(result.status_code)
```

### 204

Payment order was successfully settled

### 403

API Error

Example:

```python
{
  "errors": [
    {
      "description": "This operation cannot be completed under certain conditions",
      "error": "operation_forbidden"
    }
  ]
}
```

### 404

Payment order could not be found.

`payment_order_id` does not match a payment order

### 422

Validation Error

Example:

```python
{
  "errors": [
    {
      "description": "null value where string expected",
      "error": "null_value",
      "property": "open_banking.success_url"
    }
  ]
}
```

## Example Usage

```python
payments_api = PaymentsApi(
  tenant_id = '55555555-5555-5555-5555-555555555555',
  environment = 'sandbox'
)
payment_order_id = '55555555-5555-5555-5555-555555555555'

result = payments_api.paymentOrder.settle_payment_order(payment_order_id, fast_forward=False)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```
