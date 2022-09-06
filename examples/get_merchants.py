import os
from dotenv import load_dotenv
from ping.payments_api import PaymentsApi
from tests.test_helper import testHelper

load_dotenv()

tenant_id = os.getenv("TENANT_ID")
payments_api = PaymentsApi(tenant_id)
order_Id = testHelper.prepare_payment_order_handling()
result = payments_api.paymentOrder.split(order_Id, fast_forward=True)
if result.is_success():
 print(result.body)
 print("success")
elif result.is_error():
 print(result.errors)
 print("error")
