# Tenant Class Documentation

| Parameter     | Type     | Description                                                                   |
| ------------- | -------- | ----------------------------------------------------------------------------- |
| `tenant_id`   | `string` | The ID given to the tenant by Ping Payments                                   |
| `environment` | `string` | The API environment <br><br>Default: `production` <br><br>Optional: `sandbox` |

The API tenant can be initialized as follows:

```python
from ping.tenant import Tenant

tenant = Tenant(
  tenant_id = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
  environment = 'sandbox'
)
```

## Make Calls to the API with tenant

```python
from ping.tenant import Tenant

tenant = Tenant(
  tenant_id = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
  environment = 'sandbox'
)
merchant = tenant.merchants()
list_of_merchants = merchants.get_merchants()
print(list_of_merchants.text)
```

## Ping Payments tenant

The gateway for the SDK. This class acts as a factory for the APIs resources and hold the configuration of the SDK.

## API Resources

| Name           | Description                   |
| -------------- | ----------------------------- |
| merchants      | Gets merchants endpoints      |
| payment_orders | Gets payment orders endpoints |
| payments       | Gets payments endpoints       |
