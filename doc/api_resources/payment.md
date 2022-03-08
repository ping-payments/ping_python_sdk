# Payments

## Module Name

`payments`

## Functions

- [Initiate Payment](/doc/api_resources/merchant.md#initiate-payment)
- [Get Payment](/doc/api_resources/merchant.md#get-payment)

# Initiate Payment

Initiates a payment for a payment order.

This endpoint requires that you send in a `tenant_id`, a `payment_order_id` and an `object` of data regardning the payment. If everything is sent in correct, you will be returned a json object containing a status code of 200 and data regarding the next step towards completing the payment. If something went wrong you will either get a status code of 403, 404, 422 or 500 (for more information, go to Response Types).

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
