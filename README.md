# Ping Payments Python SDK

[![Tests](https://github.com/youcal/ping_python_sdk/actions/workflows/tests.yml/badge.svg)](https://github.com/youcal/ping_python_sdk/actions/workflows/tests.yml)
[![PyPI version](https://badge.fury.io/py/ping-sdk.svg)](https://badge.fury.io/py/ping-sdk)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This Python library manages the Ping Payments API. The Ping Payments Python SDK has endpoints for merchants, payment orders, payments and payouts.

## Table of contents

-   [Requirements](#requirements)

-   [Installation](#installation)

-   [Payments API](#payments-api)

## Requirements

The Ping Payments Python SDK supports the following versions of Python:

-   Python 3, versions 3.6 and later

## Installation

Install the latest SDK using pip:

```sh
pip install ping-sdk
```

## Payments API

### [Payments API]

-   [Merchant]

-   [Payment Orders]

-   [Payment]

-   [Payout]

-   [Ping]

### Usage

First time using Payments API? Here’s how to get started:

#### Get a tenant ID

Ping Payments provides you with a tenant ID. The Payments API uses the tenant ID to manage available resources. 

Tenant IDs connect to resource permissions.

**Important:** Make sure you store and access the tenant ID securely.

Using the Payments API:

-   Import the PaymentsAPI class
-   Instantiate a PaymentsAPI object
-   Initialize the PaymentsAPI object with the appropriate tenant ID and environment

Detailed instructions:

1. Import the PaymentsApi class from the Ping Python SDK module:

```python

from ping.payments_api import PaymentsApi

```

2. Instantiate a PaymentsApi object and initialize it with the tenant ID and the environment that you want to use.

Initialize the PaymentsApi in sandbox mode:

```python

payments_api = PaymentsApi(
		tenant_id = '55555555-5555-5555-5555-555555555555',
		environment = 'sandbox'
)

```

Initialize the PaymentsApi in production mode:

```python

payments_api = PaymentsApi(
		tenant_id = '55555555-5555-5555-5555-555555555555',
		environment = 'production'
)

```

You can ping the API connection for testing. A working connection will return `pong`.

```python

payments_api.ping.ping_the_api()

```

#### Get an Instance of an API object and call its methods

The API is implemented as a class. You work with an API by calling methods in the PaymentsApi object.

**Work with the API by calling the methods on the API object.** For example, you call get_merchants for a list of all merchants for a tenant:

```python

result = payments_api.merchant.get_merchants()

```

The SDK documentation contains a list of methods for the API class.

#### Handle the response

API calls return an ApiResponse object. Properties of the ApiResponse object describe the request (headers and request) and the response (status_code, reason_phrase, text, errors, body, and cursor). Here’s how to handle the response:

**Check whether the response succeeded or failed.**  Two helper methods in the ApiResponse object determine the success or failure of a call:

```python

if result.is_success():
	# Display the response as text
	print(result.text)
# Call the error method to see if the call failed
elif result.is_error():
	print(f"Errors: {result.errors}")

```

[//]: # "Link anchor definitions"
[payments api]: doc/payments_api.md
[merchant]: doc/api_resources/payments_api/merchant.md
[payment orders]: doc/api_resources/payments_api/paymentOrder.md
[payment]: doc/api_resources/payments_api/payment.md
[payout]: doc/api_resources/payments_api/payout.md
[ping]: doc/api_resources/payments_api/ping.md
