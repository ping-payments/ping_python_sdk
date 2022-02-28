# Merchants

```python
def __init__(self, tenant_id):
  self.base_url = 'http://sandbox.pingpayments.com/payments'
  self.tenant_id = tenant_id
```

## Class Name

`Merchants`

## Methods

- [Get Merchants](/doc/api_resources/merchant.md#get-merchants)
- [Create New Merchant](/doc/api_resources/merchant.md#create-new-merchant)
- [Get Specific Merchant](/doc/api_resources/merchant.md#get-specific-merchant)

# Get Merchants

Gets and returns an object of all the merchants under a specific tenant

You need to create an Tenant-object with a tenant_id as a parameter to access the get_merchant()-function. If the tenant_id exists, the function will return an object containing a list of all merchants under that specific tenant_id and a status_code of 200. Otherwise the status_code will be 422 and no merchants are returned.

```python
def get_merchant(self)
```

## Response Type

[`Get Merchants Response`] preliminär

## Example Usage

```python
tenant_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
tenant_object = Tenant(tenant_id)

merchants = tenant_object.merchants()
list_of_merchants = merchants.get_merchants()
print(list_of_merchants.text)
print(list_of_merchants.status_code)
```

# Create New Merchant

Creates a new merchant for a tenant.

You need to create an Tenant-object with a tenant_id as a parameter to access the create_new_merchant()-function. The function itself requires an object containing a merchant name and an organisation number as a parameter. If all parameters are correct, an object will be returned containing the merchant you created and status-code 200. If the status-code is 422, it means either that the tenant_id is wrong or that the parameter isn't an object or that the object is containing wrong datatypes.

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
tenant_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
tenant_object = Tenant(tenant_id)

merchant_object = {
  name: "example-name"
  organisation_number: "xxxxxxxxxx"
}

merchants = tenant_object.merchants()
created_merchant = merchants.create_new_merchant(merchant_object)
print(created_merchant.text)
print(created_merchant.status_code)
```

# Get Specific Merchant

Gets a specific merchant for a tenant.

You need to create an Tenant-object with a tenant_id as a parameter to access the get_specific_merchant()-function. The function itself requires a merchant_id as a parameter. If the tenant_id exists and has a merchant with the parameters merchant_id then a merchant-object containing that merchant and status_code 200 will be returned. If the tenant_id or merchant_id don't match with existing id:s, a status_code 422 will be returned instead.

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
tenant_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
tenant_object = Tenant(tenant_id)
merchant_id = "xxxxxxxxxx"

merchants = tenant_object.merchants()
specific_merchant = merchants.get_specific_merchant(merchant_id)
print(specific_merchant.text)
print(specific_merchant.status_code)
```
