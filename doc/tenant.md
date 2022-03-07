# Tenant Class Documentation

| Parameter     | Type     | Description                                                                   |
| ------------- | -------- | ----------------------------------------------------------------------------- |
| `tenant_id`   | `string` | The ID given to the tenant by Ping Payments                                   |
| `environment` | `string` | The API environment <br><br>Default: `production` <br><br>Optional: `sandbox` |

The API tenant can be initialized as follows:

```python
from ping.tenant import Tenant

tenant = Tenant(
  tenant_id = '55555555-5555-5555-5555-555555555555',
  environment = 'sandbox'
)
```

## Make Calls to the API with tenant

```python
from ping.tenant import Tenant

tenant = Tenant(
  tenant_id = '55555555-5555-5555-5555-555555555555',
  environment = 'sandbox'
)
list_of_merchants = tenant.get_merchants()
print(list_of_merchants.text)
```

## Ping Payments tenant

The gateway for the SDK. This class acts as a factory for the APIs resources and hold the configuration of the SDK.

## API Resources

| Name                  | Description                                            |
| --------------------- | ------------------------------------------------------ |
| get_merchants         | Calls `get_merchant` from the merchant module          |
| create_new_merchant   | Calls `create_new_merchant` from the merchant module   |
| get_specific_merchant | Calls `get_specific_merchant` from the merchant module |
