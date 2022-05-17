---
title: "Ping"
excerpt: "A description of the usage of the Ping endpoint"
---

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

Call `ping_the_api()` to verify that the payments API is up and can be reached with a given tenant ID.

Using ping_the_api():

-   Create a PaymentsApi object with a `tenant_id` as a parameter to access ping_the_api().
-   Send in an environment parameter to test your code in `sandbox` mode. The default value is `production`.

ping_the_api() returns a response with the text "pong" if the server can be reached and the tenant_id is valid.

```python
def ping_the_api()
```

## Response Type

```python
  result = payments_api.ping.ping_the_api()
  print(result.status_code)
```

### 200

A successful call. `ping_the_api()` returns a response with the text "pong".

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
