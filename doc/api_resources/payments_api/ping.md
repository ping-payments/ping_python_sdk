# Ping

```python
from ping.payments_api import PaymentsApi
payments_api = PaymentsApi(
  tenant_id = '55555555-5555-5555-5555-555555555555',
  environment = 'sandbox'
)
payments_api.ping.ping_the_api()
```

## Module Name

`ping`

# Ping The API

Pings the API to verify that it is reachable.

You need to create a PaymentsApi object with a `tenant_id` as a parameter to access `get_payouts()`. You can also send in an environment parameter if you wish to test your code towards a `sandbox` environment but the default value is `production`. This function will return "pong" if the API is reachable.

```python
def get_payouts(date_from=None, date_to=None)
```

## Response Type

```python
  result = payments_api.ping.ping_the_api()
  print(result.status_code)
```

### 200

Successfully pinged the API. "pong" will be returned.

Example:

```python
pong
```

## Example Usage

```python
payments_api = PaymentsApi(
  tenant_id = '55555555-5555-5555-5555-555555555555',
  environment = 'sandbox'
)

result = payments_api.ping.ping_the_api()

if result.is_success():
    print(result.body)
    print("API is reachable")
elif result.is_error():
    print("error")
    print("API is not reachable")
```
