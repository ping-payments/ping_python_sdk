# Payments

```python
from ping.payments_api import PaymentsApi
payments_api = PaymentsApi(
  tenant_id = '55555555-5555-5555-5555-555555555555',
  environment = 'sandbox'
)
payments_api.payment.initiate_payment()
payments_api.payment.get_payment()
```

## Module Name

`payments`

## Functions

-   [Initiate Payment](/doc/api_resources/payments_api/payment.md#initiate-payment)
-   [Get Payment](/doc/api_resources/payments_api/payment.md#get-payment)

# Initiate Payment

Initiates a payment for a payment order.

You need to create a PaymentsApi object with a `tenant_id` as a parameter to access `initiate_payment()`. You can also send in an environment parameter if you wish to test your code towards a `sandbox` environment but the default value is `production`. This endpoint requires that you send in a `payment_order_id` and an `object` of data regardning the payment. If everything is sent in correct, you will be returned a json object containing data regarding the next step towards completing the payment. If something went wrong you will be returned an error object).

```python
def initiate_payment(payment_object, payment_order_id)
```

| Parameter          | Type     | Description                                                       |
| ------------------ | -------- | ----------------------------------------------------------------- |
| `payment_object`   | `object` | An obejct containing all information needed to initiate a payment |
| `payment_order_id` | `string` | An ID of a specific Payment Order                                 |

## payment_object

| Containing                   | Type               | Required | Description                                                                                                                                                                                                                                                                |
| ---------------------------- | ------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `currency`                   | `string`           | Yes      | Enum: `SEK`, `NOK` <br>Type of currency used for this payment                                                                                                                                                                                                              |
| `metadata`                   | `object`           | No       | Set of key-value pairs for storing additional information about the Payment                                                                                                                                                                                                |
| `method`                     | `string`           | Yes      | Enum: `e-commerce`, `m-commerce`, `pis`,`card`,`invoice`,`autogiro` <br>The payment method for this payment                                                                                                                                                                |
| `order_items`                | `array of objects` | Yes      | An array of the items of purchase. The object contains an `amount`(an integer in cents of the given currency),a string with a `merchant_id` (of the merchant that is paying for that item), a `name`(name of the item) and a `vat_rate`(the vat rate of the item, integer) |
| `provider`                   | `string`           | Yes      | Enum: `swish`,`open_banking`,`verifone`,`billmate`,`bankgirot`, `payment_iq` <br>The payment method provider                                                                                                                                                               |
| `provider_method_parameters` | `object`           | Yes      | An object of the required fields for the given payment method provider                                                                                                                                                                                                     |
| `status_callback_url`        | `string`           | No       | The URL where you want you callback status updates on the payment                                                                                                                                                                                                          |
| `total_amount`               | `integer`          | Yes      | The total sum of all the payments                                                                                                                                                                                                                                          |

## provider_method_parameters

The diffrent `provider_method_parameters` needed for each provider. Remember to write these as objects

### Swish - method: E-Commerce

| Containing     | Type     | Required | Description                               |
| -------------- | -------- | -------- | ----------------------------------------- |
| `message`      | `string` | Yes      | A message associated with the payment.    |
| `phone_number` | `string` | Yes      | A swish connected phone number of a payer |

### Swish - method: M-Commerce

| Containing    | Type      | Required | Description                                                                                                                            |
| ------------- | --------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `message`     | `string`  | Yes      | A message associated with the payment.                                                                                                 |
| `qr_border`   | `integer` | no       | QR-code image border size in pixels. Default is 0                                                                                      |
| `qr_format`   | `string`  | no       | QR code image format. Enum: `transparent_svg`, `transparent_png`, `solid_jpg`, `solid_svg`, `solid_png `. Default is `transparent_svg` |
| `qr_size`     | `integer` | no       | QR code image size in pixels. Default is 300                                                                                           |
| `use_qr_code` | `boolean` | no       | Generate a QR code for the Swish payment. Default is false.                                                                            |

### Open Banking - method: pis

| Containing    | Type     | Required | Description                                                                |
| ------------- | -------- | -------- | -------------------------------------------------------------------------- |
| `cancel_url`  | `string` | Yes      | An URL to which the user is directed to if the payment gets canceled       |
| `error_url`   | `string` | Yes      | An URL to which the user is directed to if the payment fails               |
| `reference`   | `string` | Yes      | Reference visible in the payers and payees bank account log                |
| `success_url` | `string` | Yes      | An URL to which the user is directed to at the end of a successful payment |

### Verifone - method: card

| Containing    | Type     | Required | Description                                                                     |
| ------------- | -------- | -------- | ------------------------------------------------------------------------------- |
| `cancel_url`  | `string` | Yes      | An URL which the payer is directed to when a payment gets canceled              |
| `email`       | `string` | Yes      | The email address of a payer                                                    |
| `first_name`  | `string` | Yes      | The first name of a payer                                                       |
| `last_name`   | `string` | Yes      | The last name of a payer                                                        |
| `success_url` | `string` | Yes      | An URL to which the payer is directed to when successfully completing a payment |

### Billmate - method: invoice

| Containing            | Type      | Required | Description                                                      |
| --------------------- | --------- | -------- | ---------------------------------------------------------------- |
| `care_of`             | `string`  | No       | The payers care of (C/O) address                                 |
| `country`             | `string`  | Yes      | The payers country of residence                                  |
| `customer_reference`  | `string`  | Yes      | The customer reference                                           |
| `email`               | `string`  | Yes      | The email address of a payer                                     |
| `first_name`          | `string`  | Yes      | The first name of a payer                                        |
| `free_text`           | `string`  | No       | A free text on the invoice                                       |
| `ip_address`          | `string`  | Yes      | The IP address of the device that the payment is being made from |
| `is_company_customer` | `boolean` | Yes      | Whether or not the payer is paying as a company                  |
| `last_name`           | `string`  | Yes      | The last name of a payer                                         |
| `national_id_number`  | `string`  | Yes      | The payers national ID number                                    |
| `phone_number`        | `string`  | Yes      | The payers phone number                                          |

### Bankgirot - method: autogiro

| Containing   | Type     | Required | Description                       |
| ------------ | -------- | -------- | --------------------------------- |
| `mandate_id` | `string` | Yes      | Ping Payments Autogiro mandate ID |

### Payment Iq - method: card

| Containing    | Type     | Required | Description                                                                |
| ------------- | -------- | -------- | -------------------------------------------------------------------------- |
| `error_url`   | `string` | Yes      | An URL to which the user is directed to if the payment fails               |
| `success_url` | `string` | Yes      | An URL to which the user is directed to at the end of a successful payment |

## Response Type

```python
  result = payments_api.payment.initiate_payment(payment_object, payment_order_id)
  print(result.status_code)
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
  payments_api = PaymentsApi(
    tenant_id = '55555555-5555-5555-5555-555555555555',
    environment = 'sandbox'
  )
  payment_order_id = "55555555-5555-5555-5555-555555555555"

  payment_object = {
    "currency": "SEK",
    "metadata": {
      "delivery_id": "368745"
    },
    "total_amount": 9400,
    "method": "mobile",
    "order_items": [
      {
        "amount": 2500,
        "merchant_id": "55555555-5555-5555-5555-555555555555",
        "name": "Delivery, Pasta (Pasta Place)",
        "vat_rate": 12
      },
      {
        "amount": 6900,
        "merchant_id": "55555555-5555-5555-5555-555555555555",
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

  result = payments_api.payment.initiate_payment(payment_object, payment_order_id)
  if result.is_success():
    print(result.body)
    print("success")
  elif result.is_error():
    print(result.errors)
```

# Get Payment

Gets a payment from a payment order.

You need to create a PaymentsApi object with a `tenant_id` as a parameter to access `get_payment()`. You can also send in an environment parameter if you wish to test your code towards a `sandbox` environment but the default value is `production`. This endpoint requires you to send in a `payment_order_id` and a `payment_id` that is connected to the given payment order. If everything is correct, you will be returned a json object of that payment. If something is incorrect, you will be returned an error object containing possible information about the error.

```python
def get_payment(payment_order_id, payment_id)
```

| Parameter          | Type   | Description                                             |
| ------------------ | ------ | ------------------------------------------------------- |
| `payment_order_id` | string | A string cointaining the Id of a specific payment order |
| `payment_id`       | string | A string cointaining the Id of a specific payment       |

## Response Type

```python
  result = payments_api.payment.get_payment(payment_order_id, payment_id)
  print(result.status_code)
```

### 200

Successfully returned a payment. A json object containing the payment has been returned.

Example:

```python
{
  "currency": "SEK",
  "id": "55555555-5555-5555-5555-555555555555",
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
  payments_api = PaymentsApi(
    tenant_id = '55555555-5555-5555-5555-555555555555',
    environment = 'sandbox'
  )
  paymen_order_id = "55555555-5555-5555-5555-555555555555"
  payment_id = "55555555-5555-5555-5555-555555555555"

  result = payments_api.payment.get_payment(paymen_order_id, payment_id)
  if result.is_success():
    print(result.body)
    print("success")
  elif result.is_error():
    print(result.errors)
```
