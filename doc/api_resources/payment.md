# Payments

## Module Name

`payments`

## Functions

- [Initiate Payment](/doc/api_resources/merchant.md#initiate-payment)
- [Get Payment](/doc/api_resources/merchant.md#get-payment)

# Initiate Payment

Initiates a payment for a payment order.

You need to create a Tenant object with a `tenant_id` as a parameter to access `initiate_payment()`.This endpoint requires that you send in a `payment_order_id` and an `object` of data regardning the payment. If everything is sent in correct, you will be returned a json object containing a status code of 200 and data regarding the next step towards completing the payment. If something went wrong you will either get a status code of 403, 404, 422 or 500 (for more information, go to Response Types).

```python
def initiate_payment(payment_object, payment_order_id)
```

| Parameter          | Type     | Description                                                       |
| ------------------ | -------- | ----------------------------------------------------------------- |
| `payment_object`   | `object` | An obejct containing all information needed to initiate a payment |
| `payment_order_id` | `string` | An ID of a specific Payment Order                                 |

## Payment Object

| Containing                   | Type               | Required | Description                                                                                                                                                                                                                |
| ---------------------------- | ------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `currency`                   | `string`           | Yes      | Enum: `SEK`, `NOK` <br>Type of currency used for this payment                                                                                                                                                              |
| `merchant_amounts`           | `object`           | Yes      | An object mapping a `merchant_id` to the amount of the payment intended for them. The values are written in cents of the given currency. The total sum of the values must be equal as the total sum of all the order items |
| `metadata`                   | `object`           | No       | Set of key-value pairs for storing additional information about the Payment                                                                                                                                                |
| `method`                     | `string`           | Yes      | Enum: `mobile`, `pis`,`card`,`invoice`,`autogiro` <br>The payment method for this payment                                                                                                                                  |
| `order_items`                | `array of objects` | Yes      | An array of the items of purchase. The object contains an `amount`(in cents of the given currency),a `name`(name of the item) and a `vat_rate`(the vat rate of the item)                                                   |
| `provider`                   | `string`           | Yes      | Enum: `swish`,`open_banking`,`verifone`,`billmate`,`bankgirot` <br>The payment method provider                                                                                                                             |
| `provider_method_parameters` | `object`           | Yes      | An object of the required fields for the given payment method provider                                                                                                                                                     |
| `status_callback_url`        | `string`           | Yes      | The URL where you want you callback status updates on the payment                                                                                                                                                          |

## Response Type

```python
  _response = tenant.initiate_payment(payment_object, payment_order_id)
  print(_response.status_code)
```

### 200

Successfully initiated a payment. A json object containing information on how to procede and the payment id has been returned

Example:

```python
{
  "id": "555555-5555-5555-5555-555555555555"
  "swish": {
    "swish_url": "swish://paymentrequest?token=c28a4061470f4af48973bd2a4642b4fa&callbackurl=merchant%253A%252F%252F"
  }
}
```

### 403

API Error

Example:

```python
{
  "errors": [
    {
      "description": "Cannot initiate new Payments when PaymentOrder has been closed",
      "error": "payment_order_closed"
    }
  ]
}
```

### 404

Payment Order could not be found. the given `payment_order_id` does not match a Payment Order

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

### 500

Server Error

Example:

```python
{
  "errors": [
    {
      "description": null,
      "error": "callback_url_not_found"
    }
  ]
}
```

## Example Usage

```python
 tenant_id = "a2a4f648-a50b-42fb-bda8-00c6e2f295ea"
  tenant = Tenant(tenant_id= tenant_id)
  payment_order_id = "bd3e750f-2213-45c5-9d02-0dbeb2178675"

  payment_object = {
    "currency": "SEK",
    "merchant_amounts": {
      "075b5c3c-3f17-435d-ab84-0bc57d8e67d4": 9400,
    },
    "metadata": {
      "delivery_id": "368745"
    },
    "method": "mobile",
    "order_items": [
      {
        "amount": 2500,
        "name": "Delivery, Pasta (Pasta Place)",
        "vat_rate": 12
      },
      {
        "amount": 6900,
        "name": "Pasta (Pasta Place)",
        "vat_rate": 12
      }
    ],
    "provider": "swish",
    "provider_method_parameters": {
      "message": "Pasta from Pasta Place",
      "phone_number": "0700000000"
    },
    "status_callback_url": "https://somesite.com/callback"
  }
  _response = tenant.initiate_payment(payment_object, payment_order_id)
  print(_response.text)
```

# Get Payment

Gets a payment from a payment order.

You need to create a Tenant object with a `tenant_id` as a parameter to access `get_payment()`. This endpoint requires you to send in a `payment_order_id` and a `payment_id` that is connected to the given payment order. If everything is correct, you will be returned a json object of that payment. If something is incorrect, you will be returned an error object containing possible information about the error.

```python
def get_payment(payment_order_id, payment_id)
```

| Parameter          | Type   | Description                                             |
| ------------------ | ------ | ------------------------------------------------------- |
| `payment_order_id` | string | A string cointaining the Id of a specific payment order |
| `payment_id`       | string | A string cointaining the Id of a specific payment       |

## Response Type

### 200

Successfully initiated a payment. A json object containing information on how to procede and the payment id has been returned

Example:

```python
{
  "currency": "SEK",
  "id": "380cad75-db1a-4aa4-b19c-7581148d7174",
  "metadata": {
    "delivery_id": "230955"
  },
  "method": "mobile",
  "order_items": [
    {
      "amount": 850,
      "name": "Utkörning, Pizza",
      "vat_rate": 12
    }
  ],
  "provider": "swish",
  "status": "PENDING"
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

Payment could not be found.

The given `payment_id` cannot be found in the given `payment_order_id`.
The given `payment_order_id` don't match a payment order.

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
tenant_id = "a2a4f648-a50b-42fb-bda8-00c6e2f295ea"
tenant = Tenant(tenant_id= tenant_id)
paymen_order_id = "bd3e750f-2213-45c5-9d02-0dbeb2178675"
payment_id = "9e6333c6-a9c3-4883-98d8-1f9ef6f1955b"

payment = tenant.get_payment(paymen_order_id, payment_id)
print(payment.text)
```
