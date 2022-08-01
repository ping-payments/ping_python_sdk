
import os
from dotenv import load_dotenv
from ping.payments_api import PaymentsApi


load_dotenv()
tenant_id = os.getenv("TENANT_ID")
payment_links_api = PaymentsApi(tenant_id)

response = payment_links_api.merchant.list()
print(response)
