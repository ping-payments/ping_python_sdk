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
```

# Create New Merchant

Creates a new merchant for a tenant.

You need to create an Tenant-object with a tenant_id as a parameter to access the create_new_merchant()-function. The function itself requires an object containing a merchant name and an organisation number. If all parameters are correct, an object will be returned containing the merchant you created and status-code 200. If the status-code is 422, it means either that the tenant_id is wrong or that the parameter isn't an object or that the object is containing wrong datatypes.

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
print(created_merchant)
print(created_mercahnt.status_code)
```
