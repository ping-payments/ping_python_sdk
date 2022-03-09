from ping.configuration import get_base_url

tenant_id = None 
environment = None 
base_url = get_base_url(environment)
headers = {
      "Accept": "application/json",
      "tenant_id": tenant_id
    }

from tenant import *