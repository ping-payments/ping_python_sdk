from ping.configuration import get_base_url


tenant_id = None 
environment = "sandbox" 
base_url = get_base_url(environment)
headers = {
    "Accept": "application/json",
    "tenant_id": tenant_id
  }


from ping.tenant import *


