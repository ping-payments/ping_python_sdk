import requests
import json

def create_new_merchants():
    url = 'http://sandbox.pingpayments.com/payments/api/v1/merchants'

    header = {
        "Accept": "application/json",
        "tenant_id": "a2a4f648-a50b-42fb-bda8-00c6e2f295ea"
    }
    payload = {
        "name": "Ludvig AB",
        "organization_number": "5551355555"
    }
    
   
    r = requests.post(url, headers=header,json=payload)
    print(r.status_code)











def get_merchants():
    url = 'http://sandbox.pingpayments.com/payments/api/v1/merchants'
    header = {
        "Accept": "application/json",
        "tenant_id": "a2a4f648-a50b-42fb-bda8-00c6e2f295ea"
    }

    r = requests.get(url, headers=header)
    parsed = r.json()
    print(parsed)


create_new_merchants()
