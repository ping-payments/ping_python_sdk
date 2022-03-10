from dataclasses import dataclass
from email.mime import base
from ping.configuration import get_base_url


values = {}

def set_values(tenant_id, environment= "sandbox"):
  values.update({
    "base_url": get_base_url(environment), 
    "headers": {
      "Accept": "application/json",
      "tenant_id": tenant_id
    }})

from ping.tenant import *


