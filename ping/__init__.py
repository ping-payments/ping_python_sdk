from ping.api.payments_api import PaymentsApi

def payments_api(tenant_id="", environment="sandbox"):
    return PaymentsApi(tenant_id, environment)
