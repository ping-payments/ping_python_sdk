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

Gets and returns an object of all the payouts and optionally between dates.

You need to create a PaymentsApi object with a `tenant_id` as a parameter to access `get_payouts()`. You can also send in an environment parameter if you wish to test your code towards a `sandbox` environment but the default value is `production`. This function can also take two dates as optional parameters if you wish to get all `payouts` between two dates. If the tenant_id exists and the optional dates are valid, the function will return an object containing a list of payment orders. Otherwise an error object is returned.

```python
def get_payouts(date_from=None, date_to=None)
```

The date-time parameters follow the ISO Timestamp format (e.g. 2022-03-27T09:42:30Z)

| Parameter   | Type                 | Required | Format   | Description                                       |
| ----------- | -------------------- | -------- | -------- | ------------------------------------------------- |
| `date_from` | `string($date-time)` | No       | ISO 8601 | Start date to find payment orders after that date |
| `date_to`   | `string($date-time)` | No       | ISO 8601 | End date to find payment orders before that date  |

## Response Type

```python
  result = payments_api.payout.get_payouts()
  print(result.status_code)
```

### 200

Successfully got payouts. A json object containing an array of all the payouts for the given tenant has been returned.

Example:

```python
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

Gets a specific payout with a `payout_id`.

You need to create a PaymentsApi object with a `tenant_id` as a parameter to access `get_payout()`. You can also send in an environment parameter if you wish to test your code towards a `sandbox` environment but the default value is `production`. The function itself requires a `payou_id` as a parameter. If the `tenant_id` exists and has a payout with that `payout_id` then an object containing that payout will be returned. Otherwise an error object is returned.

```python
def get_payout(payout_id)
```

| Parameter   | Type     | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| `payout_id` | `string` | A string containing the ID of a specific payout |

## Response Type

```python
  result = payments_api.payout.get_payout(payout_id)
  print(result.status_code)
```

### 200

Successfully returned a payout. A json object containing a specific payout with the given `payout_id` has been returned.

Example:

```python
{
  "amount": 0,
  "completed_at": "string",
  "currency": "SEK",
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
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

Payout could not be found.

The given `payout_id` could not be found.

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
payout_id = '55555555-5555-5555-5555-555555555555'

result = payments_api.payout.get_payout(payout_id)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```
