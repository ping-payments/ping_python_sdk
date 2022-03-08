import requests

def initiate_payment(headers, base_url, object, payment_order_id):
 #Prepare URL
  _path = f'/api/v1/payment_orders/{payment_order_id}/payments'
  _url = base_url + _path

  #Prepare and execute response 
  _response = requests.post(_url, headers=headers, json=object)
  return _response

def get_payment(headers, base_url, payment_order_id, payment_id):
  
  _path = f'/api/v1/payment_orders/{payment_order_id}/payments/{payment_id}'
  _url = base_url + _path

  _response = requests.get(_url, headers=headers)
  return _response