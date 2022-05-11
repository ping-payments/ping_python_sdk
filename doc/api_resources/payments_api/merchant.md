# Merchants

```python
from ping.payments_api import PaymentsApi
payments_api = PaymentsApi(
  tenant_id = '55555555-5555-5555-5555-555555555555',
  environment = 'sandbox'
)
payments_api.merchant.get_merchants()
payments_api.merchant.create_new_merchant()
payments_api.merchant.get_specific_merchant()
```

## Module Name

`merchants`

## Functions

-   [Get Merchants](/doc/api_resources/payments_api/merchant.md#get-merchants)
-   [Create New Merchant](/doc/api_resources/payments_api/merchant.md#create-new-merchant)
-   [Get Specific Merchant](/doc/api_resources/payments_api/merchant.md#get-specific-merchant)

# Get Merchants

Gets and returns an object of all the merchants from a specific tenant

You need to create a PaymentsApi object with a `tenant_id` as a parameter to access `get_merchant()`. You can also send in an environment parameter if you wish to test your code towards a `sandbox` environment but the default value is `production`. If the tenant_id exists, the function will return an object containing a list of all merchants under that specific `tenant_id`. Otherwise an error object is returned.

```python
def get_merchants()
```

## Response Type

```python
  result = payments_api.merchant.get_merchants()
  print(result.status_code)
```

### 200

Successfully got merchants. A json object containing an array of all the merchants for the given tenant has been returned.

Example:

```python
[
  {
    "email": "contact@merchant.a.com",
    "id": "55555555-5555-5555-5555-555555555555",
    "name": "Merchant A",
    "organization": {
      "country": "NO",
      "no_organization_number": "555555555"
    },
    "phone_number": "0731231234"
  },
  {
    "email": "contact@merchant.b.com",
    "id": "55555555-5555-5555-5555-555555555555",
    "name": "Merchant B",
    "organization": {
      "country": "SE",
      "se_organization_number": "5555555555"
    },
    "phone_number": "0739876543"
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

result = payments_api.merchant.get_merchants()
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Create New Merchant

Creates a new merchant for a tenant.

You need to create a PaymentApi object with a `tenant_id` as a parameter to access `create_new_merchant()`. You can also send in an environment parameter if you wish to test your code towards a `sandbox` environment but the default value is `production`. The function itself requires an object containing a merchant name and an organisation object containing the `country` and the `organisation_number`. If all parameters are correct, an object will be returned containing an object of the merchant you created. Otherwise an error object is returned.

```python
def create_new_merchant(merchant_object)
```

| Parameter         | Type     | Containing                                      | Description                                                                                                                                                                             |
| ----------------- | -------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `merchant_object` | `object` | merchant_name:`string`<br>organisation:`object` | An object containing a name for the new merchant and an organisation object containing `contry: String` and `organisation_number: string` for the organisation that merchant is part of |

## Response Type

```python
  result = payments_api.merchant.create_new_merchant(merchant_object)
  print(result.status_code)
```

### 200

Successfully created a merchant. A json object containing that merchants has been returned.

Example:

```python
{
  "name": "Merchant",
  "organization": {
    "country": "SE",
    "se_organization_number": "5555555555"
  }
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

merchant_object = {
  "name": 'example-name',
  "organisation": {
    "country": 'SE',
    "se_organisation_number": '5555555555'
  }
}

result = payemnts_api.merchant.create_new_merchant(merchant_object)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Get Specific Merchant

Gets a specific merchant from a tenant.

You need to create a PaymentsApi object with a `tenant_id` as a parameter to access `get_specific_merchant()`. You can also send in an environment parameter if you wish to test your code towards a `sandbox` environment but the default value is `production`. The function itself requires a `merchant_id` as a parameter. If the `tenant_id` exists and has a merchant with the given `merchant_id` then a merchant object containing that specific merchant will be returned. Otherwise an error object is returned.

```python
def get_specific_merchant(merchant_id)
```

| Parameter     | Type     | Description                                       |
| ------------- | -------- | ------------------------------------------------- |
| `merchant_id` | `string` | A string containing the ID of a specific merchant |

## Response Type

```python
  result = payments_api.merchant.get_specific_merchant(merchant_id)
  print(result.status_code)
```

### 200

Successfully returned a merchant. A json object containing a specific merchant for the given tenant has been returned.

Example:

```python
{
  "email": "contact@merchant.com",
  "id": "55555555-5555-5555-5555-555555555555",
  "name": "Merchant",
  "organization": {
    "country": "SE",
    "se_organization_number": "5555555555"
  },
  "phone_number": "0705555555"
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

Merchant could not be found.

The given `merchant_id` could not be found.

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
merchant_id = '55555555-5555-5555-5555-555555555555'

result = payments_api.merchant.get_specific_merchant(merchant_id)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```
