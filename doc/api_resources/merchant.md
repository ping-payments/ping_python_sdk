# Merchants

## Module Name

`merchants`

## Functions

- [Get Merchants](/doc/api_resources/merchant.md#get-merchants)
- [Create New Merchant](/doc/api_resources/merchant.md#create-new-merchant)
- [Get Specific Merchant](/doc/api_resources/merchant.md#get-specific-merchant)

# Get Merchants

Gets and returns an object of all the merchants from a specific tenant

You need to create a Tenant object with a `tenant_id` as a parameter to access `get_merchant()`. You can also send in an environment parameter if you wish to test your code towards a `sandbox` environment but the default value is `production`. If the tenant_id exists, the function will return an object containing a list of all merchants under that specific `tenant_id` and a status code of 200. Otherwise the status code will be 422 and no merchants are returned.

```python
def get_merchants(self)
```

## Response Type

### 200

Successfully got merchants. A json object containing an array of all the merchants for the given tenant has been returned.

Example:

```python
[
  {
    "email": "contact@merchant.a.com",
    "id": "2d041d6d-21c9-4c65-96eb-5b9047732417",
    "name": "Merchant A",
    "organization": {
      "country": "NO",
      "no_organization_number": "555555555"
    },
    "phone_number": "0731231234"
  },
  {
    "email": "contact@merchant.b.com",
    "id": "2c6fec28-9316-4aa6-86c7-d1ee019a9bfa",
    "name": "Merchant B",
    "organization": {
      "country": "SE",
      "se_organization_number": "678998-1234"
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
tenant = Tenant(tenant_id = '55555555-5555-5555-5555-555555555555', environment = 'environment')

list_of_merchants = tenant.get_merchants()
print(list_of_merchants.text)
```

# Create New Merchant

Creates a new merchant for a tenant.

You need to create a Tenant object with a `tenant_id` as a parameter to access `create_new_merchant()`. You can also send in an environment parameter if you wish to test your code towards a `sandbox` environment but the default value is `production`. The function itself requires an object containing a merchant name and an organisation object containing the `country` and the `organisation_number`. If all parameters are correct, an object will be returned containing the merchant you created and status code 200. If the status code is 422, it either means that the `tenant_id` is wrong, that the parameter isn't an object or that the object is containing incorrect datatypes.

```python
def create_new_merchant(self, merchant_object)
```

| Parameter         | Type     | Containing                                      | Description                                                                                                                                                                             |
| ----------------- | -------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `merchant_object` | `object` | merchant_name:`string`<br>organisation:`object` | An object containing a name for the new merchant and an organisation object containing `contry: String` and `organisation_number: string` for the organisation that merchant is part of |

## Response Type

[`Create New Merchant Response`] preliminär

## Example Usage

```python
tenant = Tenant(tenant_id = '55555555-5555-5555-5555-555555555555', environment = 'environment')

merchant_object = {
  "name": 'example-name',
  "organisation": {
    "country": 'SE',
    "se_organisation_number": '555555-5555'
  }
}
created_merchant = tenant.create_new_merchant(merchant_object)
print(created_merchant.text)
```

# Get Specific Merchant

Gets a specific merchant from a tenant.

You need to create a Tenant object with a `tenant_id` as a parameter to access `get_specific_merchant()`. You can also send in an environment parameter if you wish to test your code towards a `sandbox` environment but the default value is `production`. The function itself requires a `merchant_id` as a parameter. If the `tenant_id` exists and has a merchant with the parameters `merchant_id` then a merchant object containing that merchant and status code 200 will be returned. If the `tenant_id` or `merchant_id` don't match with existing id:s, a status code 422 will be returned instead.

```python
def get_specific_merchant(self, merchant_id)
```

| Parameter     | Type   | Containing           | Description                                        |
| ------------- | ------ | -------------------- | -------------------------------------------------- |
| `merchant_id` | String | merchant_id : String | A string cointaining the Id of a specific merchant |

## Response Type

### 200

Successfully returned a merchant. A json object containing a specific merchant for the given tenant has been returned.

Example:

```python
{
  "email": "contact@merchant.com",
  "id": "2d041d6d-21c9-4c65-96eb-5b9047732417",
  "name": "Merchant",
  "organization": {
    "country": "SE",
    "se_organization_number": "555555-5555"
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

Merchants could not be found.

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
tenant = Tenant(tenant_id = '55555555-5555-5555-5555-555555555555', environment = 'environment')
merchant_id = '5555555555'

specific_merchant = tenant.get_specific_merchant(merchant_id)
print(specific_merchant.text)
```
