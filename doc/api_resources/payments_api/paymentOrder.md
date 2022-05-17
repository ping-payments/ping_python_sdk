---
title: "Payment Order"
excerpt: "A description of the usage of the Payment Order endpoint"
---
# Payment Order

The `payment order` endpoint exposes several methods dedicated to dealing with payment objects.

Example:

```python
from ping.payments_api import PaymentsApi
payments_api = PaymentsApi(
  tenant_id = '55555555-5555-5555-5555-555555555555',
  environment = 'sandbox'
)
payments_api.payment_order.get_payment_orders()
payments_api.payment_order.create_payment_order()
payments_api.payment_order.get_payment_order()
payments_api.payment_order.update_payment_order()
payments_api.payment_order.close_payment_order()
payments_api.payment_order.split_payment_order()
payments_api.payment_order.settle_payment_order()
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

Gets and returns a list of payment order objects connected to a `tenant_id`.

Using `get_payment_orders()`:

-   Create a PaymentsApi object with a `tenant_id` as a parameter to access get_payment_orders().
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`.

You can use the optional `date_from` and `date_to` parameters to limit the list of payment order objects get_payment_orders() returns, by date. 
get_payment_orders() returns an error object if the tenant_id is invalid or if you have provided an invalid date in either the date_from or date_to parameter. 

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
  result = payments_api.payment_order.get_payment_orders()
  print(result.status_code)
```

### 200

A successful call. `get_payment_orders()` returns a list of payment order objects.

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

API error. The payment order endpoint returned an error message.

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

Validation error. The payment order endpoint returned an error message because of an invalid value.

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

result = payments_api.payment_order.get_payment_order(
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

Creates a new payment order connected to a split tree datastructure.

Using `create_payment_order()`:

-   Create a PaymentsApi object with a `tenant_id` as a parameter to access create_payment_order()).
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`.

create_payment_order() takes a `split_tree_id` and a specified `currency` and returns an object containing a `payment_order_id`. 
create_payment_order() returns an error object if the split_tree_id or currecy is invalid.

```python
def create_payment_order(split_tree_id)
```

| Parameter       | Type     | Required | Description                                                                                                                                                 |
| --------------- | -------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `split_tree_id` | `string` | Yes      | String containing the ID of a specific split tree                                                                                                           |
| `currency`      | `string` | Yes      | Enum: `SEK`, `NOK` <br>Type of currency used for this payment order. Payments connected to a payment order must have the same currency as the payment order |

## Response Type

```python
  result = payments_api.payment_order.create_payment_order(split_tree_id)
  print(result.status_code)
```

### 200

A successful call. `create_payment_order()` created a payment order. create_payment_order() returns an object containing a new `payment_order_id`.

Example:

```python
{
  "id": "55555555-5555-5555-5555-555555555555"
}
```

### 403

API error. The payment order endpoint returned an error message.

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

Validation error. The payment order endpoint returned an error message because of an invalid value.

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

Gets a payment order.

Using `get_payment_order()`:

-   Create a PaymentsApi object with a `tenant_id` as a parameter to access get_payment_order().
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`.

create_payment_order() takes a `payment_order_id` and returns a payment order object. 
create_payment_order() returns an error object if the payment_order_id is invalid.

```python
def get_payment_order(payment_order_id)
```

| Parameter          | Type     | Description                                            |
| ------------------ | -------- | ------------------------------------------------------ |
| `payment_order_id` | `string` | String containing the ID of a specific payment order   |

## Response Type

```python
  result = payments_api.payment_order.get_payment_order(payment_order_id)
  print(result.status_code)
```

### 200

A successful call. `create_payment_order()` returned a payment order.

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

API error. The payment order endpoint returned an error message.

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

Search error. `create_payment_order()` couldn't match the `payment_order_id` to a payment order object.

### 422

Validation error. The payment order endpoint returned an error message because of an invalid value.

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

result = payments_api.payment_order.get_payment_order(payment_order_id)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Update Payment Order

Updates a payment order with a new split tree datastructure.

The new split tree datastructure is used for splitting payments in the payment order between payment recipients.

Using `update_payment_order()`:

-   Create a PaymentsApi object with a `tenant_id` as a parameter to access get_payment_order().
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`.

update_payment_order() takes a `payment_order_id` and a `split_tree_id`, and updates a payment order matching the payment_order_id. 
create_payment_order() returns an error object if the payment_order_id is invalid.

```python
def update_payment_order(payment_order_id, split_tree_id)
```

| Parameter          | Type     | Description                                            |
| ------------------ | -------- | ------------------------------------------------------ |
| `payment_order_id` | `string` | String containing the ID of a specific payment order   |
| `split_tree_id`    | `string` | String containing the ID of a specific split tree      |

## Response Type

```python
  result = payments_api.payment_order.update_payment_order(splut_tree_id)
  print(result.status_code)
```

### 204

A successful call.

### 403

API error. The payment order endpoint returned an error message.

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

Search error. `update_payment_order()` couldn't match the `payment_order_id` to a payment order or the `split_tree_id` to an existing split tree datastructure.

### 422

Validation error. The payment order endpoint returned an error message because of an invalid value.

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

result = payments_api.payment_order.update_payment_order(payment_order_id, split_tree_id)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Close Payment Order

Closes a payment order and disables the possibility of updating the payment order with further payments.

Using `close_payment_order()`:

-   Create a PaymentsApi object with a `tenant_id` as a parameter to access get_payment_order().
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`.

close_payment_order() takes a `payment_order_id` and updates a payment order matching the payment_order_id with a "closed" status.
close_payment_order() returns an error object if the payment_order_id is invalid.

```python
def close_payment_order(payment_order_id)
```

| Parameter          | Type     | Required | Description                                            |
| ------------------ | -------- | -------- | ------------------------------------------------------ |
| `payment_order_id` | `string` | Yes      | String containing the ID of a specific payment order   |

## Response Type

```python
  result = payments_api.payment_order.close_payment_order(payment_order_id)
  print(result.status_code)
```

### 204

A successful call.

### 403

API error. The payment order endpoint returned an error message.

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

Search error. `close_payment_order()` couldn't match the `payment_order_id` to a payment order.

### 422

Validation error. The payment order endpoint returned an error message because of an invalid value.

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

result = payments_api.payment_order.close_payment_order(payment_order_id)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Split Payment Order

Splits a payment order. Used when when the conditions for some payments in a payment order have been fulfilled.

A split payment order can still be partly refunded.

Using `split_payment_order()`:

-   Create a PaymentsApi object with a `tenant_id` as a parameter to access get_payment_order().
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`.

split_payment_order() takes a `payment_order_id` and updates ("splits") a payment order matching the payment_order_id. 
split_payment_order() returns an error object if the payment_order_id is invalid.

```python
def split_payment_order(payment_order_id)
```

| Parameter          | Type      | Required | Description                                                                             |
| ------------------ | --------- | -------- | --------------------------------------------------------------------------------------- |
| `payment_order_id` | `string`  | Yes      | String containing the ID of a specific payment order                                    |
| `fast_forward`     | `boolean` | No       | Boolean that indicates that a payment order shall be closed and split. Default: `false` |                  |

## Response Type

```python
  result = payments_api.payment_order.split_payment_order(payment_order_id)
  print(result.status_code)
```

### 204

A successful call.

### 403

API error. The payment order endpoint returned an error message.

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

Search error. `split_payment_order()` couldn't match the `payment_order_id` to a payment order.

### 422

Validation error. The payment order endpoint returned an error message because of an invalid value.

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

result = payments_api.payment_order.split_payment_order(payment_order_id)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Settle Payment Order

Marks a payment order as "settled". A settled payment order is slated for a future payout.

Refunds are not possible on a settled payment order.

Using `settle_payment_order()`:

-   Create a PaymentsApi object with a `tenant_id` as a parameter to access get_payment_order().
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`.

settle_payment_order() takes a `payment_order_id` and updates a payment order matching the payment_order_id with a "settled" status. 
settle_payment_order() returns an error object if the payment_order_id is invalid.


```python
def settle_payment_order(payment_order_id)
```

| Parameter          | Type      | Required | Description                                                                                                  |
| ------------------ | --------- | -------- | ------------------------------------------------------------------------------------------------------------ |
| `payment_order_id` | `string`  | Yes      | String containing the ID of a specific payment order                                                         |
| `fast_forward`     | `boolean` | No       | Boolean that indicates that a payment order shall be closed, split and settled. Default: `false`             |

## Response Type

```python
  result = payments_api.payment_order.settle_payment_order(payment_order_id)
  print(result.status_code)
```

### 204

A successful call.

### 403

API error. The payment order endpoint returned an error message.

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

Search error. `settle_payment_order()` couldn't match the `payment_order_id` to a payment order.

### 422

Validation error. The payment order endpoint returned an error message because of an invalid value.

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

result = payments_api.payment_order.settle_payment_order(payment_order_id)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```
