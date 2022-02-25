from urllib import response
import requests
import json

"""
merchant_id: df5e30b0-dd8d-44f0-b200-a734a55ce6e6
"""

class Merchants():

    def __init__(self, tenant_id):
        self.base_url = 'http://sandbox.pingpayments.com/payments'
        self.tenant_id =  tenant_id

    def get_merchants(self):
        path = '/api/v1/merchants'
        url = self.base_url + path
        header = {
            "Accept": "application/json",
            "tenant_id": self.tenant_id
        }

        response = requests.get(url, headers=header)
        return response

    def create_new_merchants(self, object):
        path = '/api/v1/merchants'
        url = self.base_url + path
        header = {
            "Accept": "application/json",
            "tenant_id": self.tenant_id
        }
        
        response = requests.post(url, headers=header,json=object)
        return response

    def get_specific_merchant(self, merchant_id):
        path = '/api/v1/merchants/'
        url = self.base_url + path + merchant_id 
        header = {
            "Accept": "application/json",
            "tenant_id": self.tenant_id
        }

        response = requests.get(url, headers=header)
        return response
