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
payments_api.paymentOrder.list()
payments_api.paymentOrder.create()
payments_api.paymentOrder.get()
payments_api.paymentOrder.update()
payments_api.paymentOrder.close()
payments_api.paymentOrder.split()
payments_api.paymentOrder.settle()
```

## Module Name

`paymentOrders`

## Functions

-   [List](/doc/api_resources/payments_api//paymentOrder.md#list-payment-orders)
-   [Create](/doc/api_resources/payments_api//paymentOrder.md#create-payment-order)
-   [Get](/doc/api_resources/payments_api//paymentOrder.md#get-payment-order)
-   [Update](/doc/api_resources/payments_api//paymentOrder.md#update-payment-order)
-   [Close](/doc/api_resources/payments_api//paymentOrder.md#close-payment-order)
-   [Split](/doc/api_resources/payments_api//paymentOrder.md#split-payment-order)
-   [Settle](/doc/api_resources/payments_api//paymentOrder.md#settle-payment-order)

# List Payment Orders

Gets and returns a list of payment order objects for a tenant.

Using `paymentOrder.list()`:

-   Create a PaymentsApi object with a `tenant_id` as a parameter to access paymentOrder.list().
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`.

You can use the optional `date_from` and `date_to` parameters to limit the list of payment order objects paymentOrder.list() returns, by date.
This function returns an error object if you have provided an invalid date in either the date_from or date_to parameter or if the tenant_id is invalid.

```python
def list(date_from=None, date_to=None)
```

The date-time parameters follow the ISO Timestamp format (e.g. 2022-03-27T09:42:30Z)

| Parameter   | Type                 | Required | Format   | Description                                       |
| ----------- | -------------------- | -------- | -------- | ------------------------------------------------- |
| `date_from` | `string($date-time)` | No       | ISO 8601 | Start date to find payment orders after that date |
| `date_to`   | `string($date-time)` | No       | ISO 8601 | End date to find payment orders before that date  |

## Response Type

```python
  result = payments_api.paymentOrder.list()
  print(result.status_code)
```

### 200

A successful call. `paymentOrder.list()` returns a list of payment order objects.

Example:

```json
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

```json
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

```json
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

result = payments_api.paymentOrder.list(
  date_to = "2000-03-27T09:42:30Z"
  date_from = "2022-03-27T09:42:30Z"
)

if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Create Payment Order

Creates a new payment order connected to a split tree datastructure.

Using `paymentOrder.create()`:

-   Create a PaymentsApi object with a `tenant_id` as a parameter to access paymentOrder.create()).
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`.

paymentOrder.create() takes a `split_tree_id` and a specified `currency` and returns an object containing a `payment_order_id`.
This function returns an error object if the split_tree_id or currecy is invalid, or if the tenant_id is invalid.

```python
def create(split_tree_id, currency)
```

| Parameter       | Type     | Required | Description                                                                                                                                                 |
| --------------- | -------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `split_tree_id` | `string` | Yes      | String containing the ID of a specific split tree                                                                                                           |
| `currency`      | `string` | Yes      | Enum: `SEK`, `NOK` <br>Type of currency used for this payment order. Payments connected to a payment order must have the same currency as the payment order |

## Response Type

```python
  result = payments_api.paymentOrder.create(split_tree_id, currency)
  print(result.status_code)
```

### 200

A successful call. `paymentOrder.create()` created a payment order. paymentOrder.create() returns an object containing a new `payment_order_id`.

Example:

```json
{
	"id": "55555555-5555-5555-5555-555555555555"
}
```

### 403

API error. The payment order endpoint returned an error message.

Example:

```json
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

```json
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

result = payemnts_api.payment_order.create(split_tree_id, currency)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Get Specific Payment Order

Gets a payment order.

Using `paymentOrder.get()`:

-   Create a PaymentsApi object with a `tenant_id` as a parameter to access paymentOrder.get().
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`.

paymentOrder.get() takes a `payment_order_id` and returns a payment order object.
This function returns an error object if the payment_order_id is invalid or if the tenant_id is invalid.

```python
def get(payment_order_id)
```

| Parameter          | Type     | Description                                          |
| ------------------ | -------- | ---------------------------------------------------- |
| `payment_order_id` | `string` | String containing the ID of a specific payment order |

## Response Type

```python
  result = payments_api.paymentOrder.get(payment_order_id)
  print(result.status_code)
```

### 200

A successful call. `paymentOrder.get()` returned a payment order.

Example:

```json
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

```json
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

Search error. `paymentOrder.get()` couldn't match the `payment_order_id` to a payment order object.

### 422

Validation error. The payment order endpoint returned an error message because of an invalid value.

Example:

```json
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

result = payments_api.paymentOrder.get(payment_order_id)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Update Payment Order

Updates a payment order with a new "split tree" datastructure containing a ruleset for the distribution of funds.

The new split tree datastructure is used for splitting payments in the payment order between payment recipients.

Using `paymentOrder.update()`:

-   Create a PaymentsApi object with a `tenant_id` as a parameter to access paymentOrder.update().
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`.

paymentOrder.update() takes a `payment_order_id` and a `split_tree_id`, and updates a payment order matching the payment_order_id.
this function returns an error object if the payment_order_id is invalid or if the tenant_id is invalid.

```python
def update(payment_order_id, split_tree_id)
```

| Parameter          | Type     | Description                                          |
| ------------------ | -------- | ---------------------------------------------------- |
| `payment_order_id` | `string` | String containing the ID of a specific payment order |
| `split_tree_id`    | `string` | String containing the ID of a specific split tree    |

## Response Type

```python
  result = payments_api.paymentOrder.update(payment_order_id, split_tree_id)
  print(result.status_code)
```

### 204

A successful call.

### 403

API error. The payment order endpoint returned an error message.

Example:

```json
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

Search error. `paymentOrder.update()` couldn't match the `payment_order_id` to a payment order or the `split_tree_id` to an existing split tree datastructure.

### 422

Validation error. The payment order endpoint returned an error message because of an invalid value.

Example:

```json
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

result = payments_api.paymentOrder.update(payment_order_id, split_tree_id)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Close Payment Order

Closes a payment order and disables the possibility of updating the payment order with further payments.

Using `paymentOrder.close()`:

-   Create a PaymentsApi object with a `tenant_id` as a parameter to access paymentOrder.close().
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`.

paymentOrder.close() takes a `payment_order_id` and updates a payment order matching the payment_order_id with a "closed" status.
This function returns an error object if the payment_order_id is invalid or if the tenant_id is invalid.

```python
def close(payment_order_id)
```

| Parameter          | Type     | Required | Description                                          |
| ------------------ | -------- | -------- | ---------------------------------------------------- |
| `payment_order_id` | `string` | Yes      | String containing the ID of a specific payment order |

## Response Type

```python
  result = payments_api.paymentOrder.close(payment_order_id)
  print(result.status_code)
```

### 204

A successful call.

### 403

API error. The payment order endpoint returned an error message.

Example:

```json
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

Search error. `paymentOrder.close()` couldn't match the `payment_order_id` to a payment order.

### 422

Validation error. The payment order endpoint returned an error message because of an invalid value.

Example:

```json
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

result = payments_api.paymentOrder.close(payment_order_id)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Split Payment Order

Splits a payment order. Used when some payments in a payment order have been fulfilled.

A split payment order can still be partly refunded.

Using `paymentOrder.split()`:

-   Create a PaymentsApi object with a `tenant_id` as a parameter to access paymentOrder.split().
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`.

paymentOrder.split() takes a `payment_order_id` and updates ("splits") a payment order matching the payment_order_id.
This function returns an error object if the payment_order_id is invalid or if the tenant_id is invalid.

```python
def split(payment_order_id, fast_forward=False)
```

| Parameter          | Type      | Required | Description                                                                             |
| ------------------ | --------- | -------- | --------------------------------------------------------------------------------------- |
| `payment_order_id` | `string`  | Yes      | String containing the ID of a specific payment order                                    |
| `fast_forward`     | `boolean` | No       | Boolean that indicates that a payment order shall be closed and split. Default: `false` |

## Response Type

```python
  result = payments_api.paymentOrder.split(payment_order_id, fast_forward=False)
  print(result.status_code)
```

### 204

A successful call.

### 403

API error. The payment order endpoint returned an error message.

Example:

```json
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

Search error. `paymentOrder.split()` couldn't match the `payment_order_id` to a payment order.

### 422

Validation error. The payment order endpoint returned an error message because of an invalid value.

Example:

```json
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

result = payments_api.paymentOrder.split(payment_order_id, fast_forward=False)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Settle Payment Order

Marks a payment order as "settled". A settled payment order only contains processed payments.

Refunds are not possible on a settled payment order.

Using `paymentOrder.settle()`:

-   Create a PaymentsApi object with a `tenant_id` as a parameter to access paymentOrder.settle().
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`.

paymentOrder.settle() takes a `payment_order_id` and updates a payment order matching the payment_order_id with a "settled" status.
This function returns an error object if the payment_order_id is invalid or if the tenant_id is invalid.

```python
def settle(payment_order_id, fast_forward=False)
```

| Parameter          | Type      | Required | Description                                                                                      |
| ------------------ | --------- | -------- | ------------------------------------------------------------------------------------------------ |
| `payment_order_id` | `string`  | Yes      | String containing the ID of a specific payment order                                             |
| `fast_forward`     | `boolean` | No       | Boolean that indicates that a payment order shall be closed, split and settled. Default: `false` |

## Response Type

```python
  result = payments_api.paymentOrder.settle(payment_order_id, fast_forward)
  print(result.status_code)
```

### 204

A successful call.

### 403

API error. The payment order endpoint returned an error message.

Example:

```json
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

Search error. `paymentOrder.settle()` couldn't match the `payment_order_id` to a payment order.

### 422

Validation error. The payment order endpoint returned an error message because of an invalid value.

Example:

```json
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

result = payments_api.paymentOrder.settle(payment_order_id, fast_forward=False)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```
