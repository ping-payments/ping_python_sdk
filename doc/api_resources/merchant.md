# Merchants

```python
merchants = tenant.merchants()
```

## Module Name

`merchants`

## Functions

- [Get Merchants](/doc/api_resources/merchant.md#get-merchants)
- [Create New Merchant](/doc/api_resources/merchant.md#create-new-merchant)
- [Get Specific Merchant](/doc/api_resources/merchant.md#get-specific-merchant)

# Get Merchants

Gets and returns an object of all the merchants from a specific tenant

You need to create an Tenant-object with a tenant_id as a parameter to access the get_merchant()-function. You can also send in an environment parameter if you wish to test your code towards a "sandbox" environment but the default value is "production". If the tenant_id exists, the function will return an object containing a list of all merchants under that specific tenant_id and a status_code of 200. Otherwise the status_code will be 422 and no merchants are returned.

```python
def get_merchant(self)
```

## Response Type

[`Get Merchants Response`] preliminär

## Example Usage

```python
tenant = Tenant(tenant_id = '55555555-5555-5555-5555-555555555555', environment = 'environment')

list_of_merchants = tenant.get_merchants()
print(list_of_merchants.text)
```

# Create New Merchant

Creates a new merchant from a tenant.

You need to create an Tenant-object with a tenant_id as a parameter to access the create_new_merchant(). You can also send in an environment parameter if you wish to test your code towards a `sandbox` environment but the default value is `production`. The function itself requires an object containing a merchant name and an organisation object containing the country and the organisation number. If all parameters are correct, an object will be returned containing the merchant you created and status-code 200. If the status-code is 422, it either means that the tenant_id is wrong, that the parameter isn't an object or that the object is containing incorrect datatypes.

```python
def create_new_merchant(self, merchant_object)
```

| Parameter         | Type   | Containing                                                | Description                                                                                                               |
| ----------------- | ------ | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `merchant_object` | Object | merchant_name: String <br><br>organisation_number: String | An object containing a name for the new merchant and the organisationnumber for the organisation that merchant is part of |

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

You need to create an Tenant-object with a tenant_id as a parameter to access the get_specific_merchant()-function. You can also send in an environment parameter if you wish to test your code towards a "sandbox" environment but the default value is "production". The function itself requires a merchant_id as a parameter. If the tenant_id exists and has a merchant with the parameters merchant_id then a merchant-object containing that merchant and status_code 200 will be returned. If the tenant_id or merchant_id don't match with existing id:s, a status_code 422 will be returned instead.

```python
def get_specific_merchant(self, merchant_id)
```

| Parameter     | Type   | Containing           | Description                                        |
| ------------- | ------ | -------------------- | -------------------------------------------------- |
| `merchant_id` | String | merchant_id : String | A string cointaining the Id of a specific merchant |

## Response Type

[`Get Specific Merchant Response`] preliminär

## Example Usage

```python
tenant = Tenant(tenant_id = '55555555-5555-5555-5555-555555555555', environment = 'environment')
merchant_id = '5555555555'

specific_merchant = tenant.get_specific_merchant(merchant_id)
print(specific_merchant.text)
```
