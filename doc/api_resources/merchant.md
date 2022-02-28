# Merchants

```python
self.base_url = 'http://sandbox.pingpayments.com/payments'
self.tenant_id =  tenant_id
```

## Class Name

`Merchants`

## Methods

- [Get Merchants](/doc/api_resources/merchant.md#get-merchants)
- [Create New Merchant](/doc/api_resources/merchant.md#create-new-merchant)
- [Get Merchant by Id](/doc/api_resources/merchant.md#get-merchant-by-id)

# Get Merchants

Gets and returns an object of all the merchants under a specific tenant

You need to create an Tenant object with a tenant_id as a parameter to access the get_merchant()-function. If the tenant_id is correct, the function will return an object containing all merchants under that specific tenant_id and a response-type of 200. Otherwise the response-type will be 422 and no merchants are returned.

```python
def get_merchant()
```

## Response Type

[`Get Merchants Response`] preliminär

## Example Usage

```python
tenantId = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
tenant_object = Tenant(tenantId)

merchants = tenant_object.merchants()
list_of_merchants = merchants.get_merchants()
print(list_of_merchants.text)
```

# Create New Merchant
