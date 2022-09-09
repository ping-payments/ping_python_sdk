import os
from dotenv import load_dotenv
from ping.payments_api import PaymentsApi

load_dotenv()

tenant_id = os.getenv("TENANT_ID")
payments_api = PaymentsApi(tenant_id)

split_tree_id = os.getenv("SPLIT_TREE_ID")
result = payments_api.paymentOrder.create(split_tree_id, "SEK")

if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
    print("error")
