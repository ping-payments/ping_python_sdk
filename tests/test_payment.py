from ping.payments_api import PaymentsApi
import unittest


payments_api = PaymentsApi("a2a4f648-a50b-42fb-bda8-00c6e2f295ea")

class TestPayment(unittest.TestCase):
    
    def test_get_specific(self):
        payment_order_id = "8a6a4586-e082-49fe-b408-b92e9dc746ec"
        payment_id = "c498dba8-bf28-4252-a16a-7c6192c05bc9"

        self.assertEqual(
            payments_api.payment.get_payment(payment_order_id, payment_id).status_code, 
            200
            )

    def test_create(self):

        payment_order_id = "8a6a4586-e082-49fe-b408-b92e9dc746ec"
        print(payments_api.payment.initiate_payment(self.payment_body_types()["swish"], payment_order_id).status_code)
        print(payments_api.payment.initiate_payment(self.payment_body_types()["open_banking"], payment_order_id).status_code)
        print(payments_api.payment.initiate_payment(self.payment_body_types()["verifone"], payment_order_id).status_code)
        print(payments_api.payment.initiate_payment(self.payment_body_types()["billmate"], payment_order_id).status_code)
        print(payments_api.payment.initiate_payment(self.payment_body_types()["bankgirot"], payment_order_id).status_code)
        self.assertEqual(
            payments_api.payment.initiate_payment(self.payment_body_types()["swish"], payment_order_id).status_code, 
            200
        )
        self.assertEqual(
            payments_api.payment.initiate_payment(self.payment_body_types()["open_banking"], payment_order_id).status_code, 
            200
        )
        self.assertEqual(
            payments_api.payment.initiate_payment(self.payment_body_types()["verifone"], payment_order_id).status_code, 
            200
        )
        self.assertEqual(
            payments_api.payment.initiate_payment(self.payment_body_types()["billmate"], payment_order_id).status_code, 
            200
        )
        self.assertEqual(
            payments_api.payment.initiate_payment(self.payment_body_types()["bankgirot"], payment_order_id).status_code, 
            200
        )


    def payment_body_types(self):
        swish = {
            "message": "Marios Pasta från Pasta La Vista",
            "phone_number": "0700000000"
        }
        open_banking = {
            "cancel_url": "https://somesite.com/callback",
            "error_url": "https://somesite.com/callback",
            "reference": "ludvig",
            "success_url": "https://somesite.com/callback"
        }
        verifone = {
            "cancel_url": "https://somesite.com/callback",
            "email": "ludde.ludde@somemail.com",
            "first_name": "fname",
            "last_name": "lname",
            "success_url": "https://somesite.com/callback"
        }
        billmate = {
            "country": "Sweden",
            "customer_reference": "reference",
            "email": "fname.lname@somemail.com",
            "first_name": "Fname",
            "ip_address": "192.168.68.144",
            "is_company_customer": True,
            "last_name": "Lname",
            "national_id_number": "000101-0101",
            "phone_number": "0700000000"
        }
        bankgirot = {
            "mandate_id": "123213"
        }

        body_swish = {
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
                    "name": "Utkörning, Marios Pasta (Pasta La Vista)",
                    "vat_rate": 12
                },  
                {   
                    "amount": 6900,
                    "name": "Marios Pasta (Pasta La Vista)",
                    "vat_rate": 12
                }
            ],
            "provider": "swish",
            "provider_method_parameters": swish,
            "status_callback_url": "https://somesite.com/callback"
        }
        body_open_banking = {
            "currency": "SEK",
            "merchant_amounts": {
            "075b5c3c-3f17-435d-ab84-0bc57d8e67d4": 9400,
            },
            "metadata": {
                "delivery_id": "368745"
            },
            "method": "pis",
            "order_items": [
                {
                    "amount": 2500,
                    "name": "Utkörning, Marios Pasta (Pasta La Vista)",
                    "vat_rate": 12
                },  
                {
                    "amount": 6900,
                    "name": "Marios Pasta (Pasta La Vista)",
                    "vat_rate": 12
                }
            ],
            "provider": "open_banking",
            "provider_method_parameters": open_banking,
            "status_callback_url": "https://somesite.com/callback"
        }
        body_verifone = {
            "currency": "SEK",
            "merchant_amounts": {
            "075b5c3c-3f17-435d-ab84-0bc57d8e67d4": 9400,
            },
            "metadata": {
                "delivery_id": "368745"
            },
            "method": "card",
            "order_items": [
                {
                    "amount": 2500,
                    "name": "Utkörning, Marios Pasta (Pasta La Vista)",
                    "vat_rate": 12
                },
                {
                    "amount": 6900,
                    "name": "Marios Pasta (Pasta La Vista)",
                    "vat_rate": 12
                }
            ],
            "provider": "verifone",
            "provider_method_parameters": verifone,
            "status_callback_url": "https://somesite.com/callback"
        }
        body_billmate = {
            "currency": "SEK",
            "merchant_amounts": {
            "075b5c3c-3f17-435d-ab84-0bc57d8e67d4": 9400,
            },
            "metadata": {
                "delivery_id": "368745"
            },
            "method": "invoice",
            "order_items": [
                {
                    "amount": 2500,
                    "name": "Utkörning, Marios Pasta (Pasta La Vista)",
                    "vat_rate": 12
                },  
                {
                    "amount": 6900,
                    "name": "Marios Pasta (Pasta La Vista)",
                    "vat_rate": 12
                }
            ],
            "provider": "billmate",
            "provider_method_parameters": billmate,
            "status_callback_url": "https://somesite.com/callback"
        }
        body_bankgirot = {
            "currency": "SEK",
            "merchant_amounts": {
            "075b5c3c-3f17-435d-ab84-0bc57d8e67d4": 9400,
            },
            "metadata": {
                "delivery_id": "368745"
            },
            "method": "autogiro",
            "order_items": [
                {
                    "amount": 2500,
                    "name": "Utkörning, Marios Pasta (Pasta La Vista)",
                    "vat_rate": 12
                },  
                {   
                    "amount": 6900,
                    "name": "Marios Pasta (Pasta La Vista)",
                    "vat_rate": 12
                }
            ],
            "provider": "bankgirot",
            "provider_method_parameters": bankgirot,
            "status_callback_url": "https://somesite.com/callback"
        }
        body_type = {
            "swish": body_swish,
            "open_banking": body_open_banking,
            "verifone": body_verifone,
            "billmate": body_billmate,
            "bankgirot": body_bankgirot
        }
        return body_type
        

if __name__ == '__main__':
    unittest.main()