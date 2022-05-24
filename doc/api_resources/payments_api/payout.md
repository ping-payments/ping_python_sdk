---
title: "Payout"
excerpt: "A description of the usage of the Payout endpoint"
---

# Payout

```python
from ping.payments_api import PaymentsApi
payments_api = PaymentsApi(
  tenant_id = '55555555-5555-5555-5555-555555555555',
  environment = 'sandbox'
)
payments_api.payout.get_payouts()
payments_api.payout.get_payout()

```

## Module Name

`payout`

## Functions

-   [Get Payouts](/doc/api_resources/payments_api//payout.md#get-payouts)
-   [Get Specific Payout](/doc/api_resources/payments_api//payout.md#get-specific-payout)

# Get Payouts

Gets and returns a list of payout objects for a tenant.

Using `get_payouts()`:

-   Create a PaymentsApi object with a `tenant_id` as a parameter to access get_payment_orders().
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`.

You can use the optional `date_from` and `date_to` parameters to limit the list of payout objects get_payouts() returns, by date. 
get_payouts() returns an error object if you have provided an invalid date in either the date_from or date_to parameter or if the tenant_id is invalid. 

```python
def get_payouts(date_from=None, date_to=None)
```

The datetime parameters follow the ISO Timestamp format (e.g. 2022-03-27T09:42:30Z)

| Parameter   | Type                 | Required | Format   | Description                                |
| ----------- | -------------------- | -------- | -------- | ------------------------------------------ |
| `date_from` | `string($date-time)` | No       | ISO 8601 | Start date to find payouts in a date range |
| `date_to`   | `string($date-time)` | No       | ISO 8601 | End date to find payouts in a date range   |

## Response Type

```python
  result = payments_api.payout.get_payouts()
  print(result.status_code)
```

### 200

A successful call. `get_payouts()` returns a list of payout objects.

Example:

```json
[
  {
    "amount": 0,
    "completed_at": "string",
    "currency": "SEK",
    "id": "55555555-5555-5555-5555-555555555555"
  }
]
```

### 403

API error. The payout endpoint returned an error message.

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

Validation error. The payout endpoint returned an error message because of an invalid value.

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

result = payments_api.payout.get_payouts(
  date_to = "2000-03-27T09:42:30Z"
  date_from = "2022-03-27T09:42:30Z"
)

if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Get Specific Payout

Gets a payout.

Using `get_payout()`:

-   Create a PaymentsApi object with a `tenant_id` as a parameter to access get_payment_orders().
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`.

get_payout() takes a `payout_id` connected to a matching payout and returns a payout object. 
get_payout() returns an error object if the payout_id or tenant_id is invalid

```python
def get_payout(payout_id)
```

| Parameter   | Type     | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| `payout_id` | `string` | String containing the ID of a specific payout |

## Response Type

```python
  result = payments_api.payout.get_payout(payout_id)
  print(result.status_code)
```

### 200

A successful call. `get_payout()` returns a payout object.

Example:

```json
{
  "amount": 0,
  "completed_at": "string",
  "currency": "SEK",
  "id": "55555555-5555-5555-5555-555555555555"
}
```

### 403

API error. The payout endpoint returned an error message.

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

Search error. `get_payout()` couldn't match the `payout_id` to a payout object.

### 422

Validation error. The payout endpoint returned an error message because of an invalid value.

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
payout_id = '55555555-5555-5555-5555-555555555555'

result = payments_api.payout.get_payout(payout_id)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```
