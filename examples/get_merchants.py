import os
from dotenv import load_dotenv
from ping.payments_api import PaymentsApi

load_dotenv()

tenant_id = os.getenv("TENANT_ID")
payments_api = PaymentsApi(tenant_id)

merchant_id = os.getenv("MERCHANT_ID")
result = payments_api.merchant.get(merchant_id)

if result.is_success():
    print(f"Success: \n {result.body}")
elif result.is_error():
    print(f"Error: {result.status_code} \n {result.errors}")
