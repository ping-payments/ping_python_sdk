import requests
from ping.helper.apiResponse import ApiResponse
from ping.helper.apiHelper import json_deserialize

def initiate_payment(headers, base_url, object, payment_order_id):
 #Prepare URL
  _path = f'/api/v1/payment_orders/{payment_order_id}/payments'
  _url = base_url + _path

  #Prepare and execute response 
  _response = requests.post(_url, headers=headers, json=object)
  decoded = json_deserialize(_response.text)
  if type(decoded) is dict:
      _errors = decoded.get('errors')
  else:
      _errors = None
  _result = ApiResponse(_response, body=decoded, errors=_errors)
  return _result

def get_payment(headers, base_url, payment_order_id, payment_id):
  
  _path = f'/api/v1/payment_orders/{payment_order_id}/payments/{payment_id}'
  _url = base_url + _path

  _response = requests.get(_url, headers=headers)
  decoded = json_deserialize(_response.text)
  if type(decoded) is dict:
      _errors = decoded.get('errors')
  else:
      _errors = None
  _result = ApiResponse(_response, body=decoded, errors=_errors)
  return _result