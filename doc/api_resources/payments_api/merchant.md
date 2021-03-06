---
title: "Merchant"
excerpt: "A description of the usage of the Merchant endpoint"
---

# Merchant

The `merchant` endpoint exposes several methods dedicated to dealing with merchant objects.

Example:

```python
from ping.payments_api import PaymentsApi
payments_api = PaymentsApi(
  tenant_id = '55555555-5555-5555-5555-555555555555',
  environment = 'sandbox'
)
payments_api.merchant.list()
payments_api.merchant.create()
payments_api.merchant.get()
```

## Module Name

`merchants`

## Functions

-   [List](/doc/api_resources/payments_api/merchant.md#list-merchants)
-   [Create](/doc/api_resources/payments_api/merchant.md#create-merchant)
-   [Get](/doc/api_resources/payments_api/merchant.md#get-merchant)

# List Merchants

Get an list of all the merchant objects connected to a specific tenant.

Using `merchant.list()`:

-   Create a PaymentsApi object with a `tenant_id` as a parameter to access merchant.get().
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`

merchant.list() returns an object with a list of all merchants for a valid tenant_id. This function returns an error object if the tenant_id is invalid.

```python
def list()
```

## Response Type

```python
  result = payments_api.merchant.list()
  print(result.status_code)
```

### Code 200

A successful call. The merchant endpoint returned a list of all the merchants objects connected to a tenant_id.

Example:

```json
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

API error. The merchant endpoint returned an error message.

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

Validation error. The merchant endpoint returned an error message because of an invalid value.

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

result = payments_api.merchant.list()
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Create Merchant

Create and connect a new merchant to a tenant.

Using `merchant.create()`:

-   Create a PaymentApi object with a `tenant_id` as a parameter to access merchant.create().
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`.
-   Call merchant.create() with an object containing a merchant name and an organisation object containing the `country` and the `organisation_number`.

merchant.create() returns an object representing the merchant you created if all parameters are correct.
This function returns an error object if one or more parameters are invalid.

```python
def create(merchant_object)
```

| Parameter         | Type     | Containing                                      | Description                                                                                                                                                                          |
| ----------------- | -------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `merchant_object` | `object` | merchant_name:`string`<br>organisation:`object` | Object containing a name for the new merchant and an organisation object containing `country: String` and `organisation_number: string` for the organisation the merchant is part of |

## Response Type

```python
  result = payments_api.merchant.create(merchant_object)
  print(result.status_code)
```

### 200

A successful call. A new merchant was created. The merchant endpoint returned the new merchant object.

Example:

```json
{
	"name": "Merchant",
	"organization": {
		"country": "SE",
		"se_organization_number": "5555555555"
	}
}
```

### 403

API error. The merchant endpoint returned an error message.

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

Validation error. The merchant endpoint returned an error message because of an invalid value.

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

merchant_object = {
  "name": 'example-name',
  "organisation": {
    "country": 'SE',
    "se_organisation_number": '5555555555'
  }
}

result = payments_api.merchant.create(merchant_object)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```

# Get Merchant

Get a specific merchant connected to a tenant.

Using `merchant.get()`:

-   You need to create a PaymentsApi object with a `tenant_id` as a parameter to access merchant.get().
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`.

mercahnt.get() needs a `merchant_id` as a parameter.
merchant.get() returns a merchant object containing a merchant if the tenant_id and merchant_id are valid and connected.
This function returns an error object if the tenant_id or the merchant_id is invalid.

```python
def get(merchant_id)
```

| Parameter     | Type     | Description                                     |
| ------------- | -------- | ----------------------------------------------- |
| `merchant_id` | `string` | String containing the ID of a specific merchant |

## Response Type

```python
  result = payments_api.merchant.get(merchant_id)
  print(result.status_code)
```

### 200

A successful call. The merchant endpoint returned a merchant object matching the `tenant_id` and `merchant_id`.

Example:

```json
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

API error. The merchant endpoint returned an error message.

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

Search error. `merchant.get()` couldn't match the combined `tenant_id` and `merchant_id`.

### 422

Validation error. The merchant endpoint returned an error message because of an invalid value.

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
merchant_id = '55555555-5555-5555-5555-555555555555'

result = payments_api.merchant.get(merchant_id)
if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
```
