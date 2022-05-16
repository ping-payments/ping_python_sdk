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

Using `initiate_payment()`:

-   Create a PaymentsApi object with a `tenant_id` as a parameter to access `initiate_payment()`.
-   Send in an environment parameter to test your code in a `sandbox` environment. The default value is `production`

`initiate_payment()` takes a `payment_order_id` and a payment object and returns an object containing data needed to fulfill the next step of a payment. `initiate_payment()` returns an error object if the `payment_order_id` or payment object is invalid.


```python
def initiate_payment(payment_object, payment_order_id)
```

| Parameter          | Type     | Description                                                       |
| ------------------ | -------- | ----------------------------------------------------------------- |
| `payment_object`   | `object` | Object containing all information needed to initiate a payment    |
| `payment_order_id` | `string` | ID of a specific Payment Order                                    |

## payment_object

| Containing                   | Type               | Required | Description                                                                                                                                                                                                                                                                |
| ---------------------------- | ------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `currency`                   | `string`           | Yes      | Enum: `SEK`, `NOK` <br>Type of currency used for this payment                                                                                                                                                                                                              |
| `metadata`                   | `object`           | No       | Set of key-value pairs for storing additional information about the payment                                                                                                                                                                                                |
| `method`                     | `string`           | Yes      | Enum: `e_commerce`, `m_commerce`, `pis`,`card`,`invoice`,`autogiro`, `dummy` <br>Payment method for this payment                                                                                                                                                           |
| `order_items`                | `array of objects` | Yes      | Array of the items of purchase. The object contains an `amount`(an integer in cents of the given currency), a string with a `merchant_id` (of the merchant that is paying for that item), a `name`(name of the item) and a `vat_rate`(the vat rate of the item, integer)   |
| `provider`                   | `string`           | Yes      | Enum: `swish`,`open_banking`,`verifone`,`billmate`,`bankgirot`, `payment_iq`, `dummy` <br>The payment method provider                                                                                                                                                      |
| `provider_method_parameters` | `object`           | Yes      | Object of the required fields for the given payment method provider                                                                                                                                                                                                        |
| `status_callback_url`        | `string`           | No       | URL for callbacks requesting status updates on a payment. Read more under [Callback](/doc/api_resources/payments_api/payment.md##Callback)                                                                                                                                 |
| `total_amount`               | `integer`          | Yes      | Total sum of all intems of purchase                                                                                                                                                                                                                                        |

## provider_method_parameters

You need `provider_method_parameters` for each provider. Write `provider_method_parameters` in object form.

### Dummy - method: Dummy

Use dummy payments in the sandbox environment. You can test if a payment is possible with a dummy payment.

| Containing               | Type     | Required | Description                                                                                                                                                           |
| ------------------------ | -------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `desired_payment_status` | `string` | Yes      | Desired payment status for the dummy payment. <br>Enum: `INITIATED`, `PENDING`, `DECLINED`, `CANCELLED`, `CRASHED`, `COMPLETED`, `EXPIRED`, `ABORTED`                 |

### Swish - method: E_Commerce

| Containing     | Type     | Required | Description                               |
| -------------- | -------- | -------- | ----------------------------------------- |
| `message`      | `string` | Yes      | Message associated with the payment       |
| `phone_number` | `string` | Yes      | Payer's swish-connected phone number      |

### Swish - method: M_Commerce

| Containing    | Type      | Required | Description                                                                                                                            |
| ------------- | --------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `message`     | `string`  | Yes      | Message associated with the payment.                                                                                                   |
| `qr_border`   | `integer` | no       | QR-code image border size in pixels. Default is 0                                                                                      |
| `qr_format`   | `string`  | no       | QR code image format. Enum: `transparent_svg`, `transparent_png`, `solid_jpg`, `solid_svg`, `solid_png `. Default is `transparent_svg` |
| `qr_size`     | `integer` | no       | QR code image size in pixels. Default is 300                                                                                           |
| `use_qr_code` | `boolean` | no       | Generate a QR code for the Swish payment. Default is false.                                                                            |

### Open Banking - method: pis

| Containing    | Type     | Required | Description                                                                  |
| ------------- | -------- | -------- | ---------------------------------------------------------------------------- |
| `cancel_url`  | `string` | Yes      | URL to which the user is directed to if the payment gets canceled            |
| `error_url`   | `string` | Yes      | URL to which the user is directed to if the payment fails                    |
| `reference`   | `string` | Yes      | Reference visible in the payer's and payee's bank account log                |
| `success_url` | `string` | Yes      | URL to which the user is directed to upon successful completion of a payment |

### Verifone - method: card

| Containing    | Type     | Required | Description                                                                     |
| ------------- | -------- | -------- | ------------------------------------------------------------------------------- |
| `cancel_url`  | `string` | Yes      | URL to which the payer is directed to when a payment gets canceled              |
| `email`       | `string` | Yes      | Payer's email address                                                           |
| `first_name`  | `string` | Yes      | Payer's first name                                                              |
| `last_name`   | `string` | Yes      | Payer's last name                                                               |
| `success_url` | `string` | Yes      | URL to which the payer is directed to upon successful completion of a payment   |

### Billmate - method: invoice

| Containing            | Type      | Required | Description                                                      |
| --------------------- | --------- | -------- | ---------------------------------------------------------------- |
| `care_of`             | `string`  | No       | Payer's care of (C/O) address                                    |
| `country`             | `string`  | Yes      | Payer's country of residence                                     |
| `customer_reference`  | `string`  | Yes      | Customer reference                                               |
| `email`               | `string`  | Yes      | Payer's email address                                            |
| `first_name`          | `string`  | Yes      | Payer's first name                                               |
| `free_text`           | `string`  | No       | Free-text field for invoice notes                                |
| `ip_address`          | `string`  | Yes      | IP address for the device that the payment is being made from    |
| `is_company_customer` | `boolean` | Yes      | Payer's status as a company or an individual                     |
| `last_name`           | `string`  | Yes      | Payer's last name                                                |
| `national_id_number`  | `string`  | Yes      | Payer's national ID number                                       |
| `phone_number`        | `string`  | Yes      | Payer's phone number                                             |

### Bankgirot - method: autogiro

| Containing   | Type     | Required | Description                       |
| ------------ | -------- | -------- | --------------------------------- |
| `mandate_id` | `string` | Yes      | Ping Payments Autogiro mandate ID |

### Payment Iq - method: card

| Containing    | Type     | Required | Description                                                                |
| ------------- | -------- | -------- | -------------------------------------------------------------------------- |
| `error_url`   | `string` | Yes      | URL to which the user is directed to after a payment failure               |
| `success_url` | `string` | Yes      | An URL to which the user is directed to after a successful payment         |

## Response Type

```python
  result = payments_api.payment.initiate_payment(payment_object, payment_order_id)
  print(result.status_code)
```

### 200

A successful call. `initiate_payment()` initiated a payment. `initiate_payment()` returns a payment id and an object containing data needed to fulfill the next step of a payment.

Example:

```python
{
  "id": "55555555-5555-5555-5555-555555555555",
  'provider_method_response': {}
}
```

### 403

API error. The payment endpoint returned an error message.

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

Validation error. The payment endpoint returned an error message because of an invalid value.

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

## Callback

A payment goes through different stages. The payment status starts as `INITIATED`, continues as `PENDING` and last becomes either `COMPLETED`, `DECLINED`, `ABORTED`, `EXPIRED` or `CRASHED`. Callbacks from the chosen `callback_url` updates payment status.

| Payment Status | Description                                                                 |
| -------------- | --------------------------------------------------------------------------- |
| `INITIATED`    | A payment has just been initiated and will start receiving status callbacks |
| `PENDING`      | A payment has been initiated and is awaiting the next action                |
| `COMPLETED`    | The payment was successfull                                                 |
| `DECLINED`     | The payment was not proccessable                                            |
| `ABORTED`      | The payment got canceled by the payer                                       |
| `EXPIRED`      | The payment timed out. Next payment action took to long                     |
| `CRASHED`      | An unexpected has error occured                                             |

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
    "method": "e_commerce",
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
      "name": "Delivery, Pizza",
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
