import requests
from ping.helper.apiResponse import ApiResponse
from ping.helper.apiHelper import json_deserialize, check_errors

def initiate_payment(headers, base_url, object, payment_order_id):
 #Prepare URL
  _path = f'/api/v1/payment_orders/{payment_order_id}/payments'
  _url = base_url + _path

  #Prepare and execute response 
  response = requests.post(_url, headers=headers, json=object)

  #deserialize and check errors  
  decoded = json_deserialize(response.text)
  _result = check_errors(response, decoded)
  return _result

def get_payment(headers, base_url, payment_order_id, payment_id):
  
  _path = f'/api/v1/payment_orders/{payment_order_id}/payments/{payment_id}'
  _url = base_url + _path

  #Prepare and execute response 
  response = requests.get(_url, headers=headers)

  #deserialize and check errors  
  decoded = json_deserialize(response.text)
  _result = check_errors(response, decoded)
  return _result