import requests

def get_payment_orders(headers, base_url, date_from=None, date_to=None):

  """Does a GET request to /api/v1/payment_orders. 
          
    Retrieves a list of payment orders. 

    Args:
      date_from (string, optional): The timestamp for the beginning of
          the reporting period, in RFC 3339 format. Default: None   
      date_to (string, optional): The timestamp for the end of
          the reporting period, RFC 3339 format. Default: None  

    Returns:
      Response: An object with the response value as well as other
      useful information such as status codes and headers.  

    Raises:
      APIException: When an error occurs while fetching the data from
      the remote API. This exception includes the HTTP Response
      code, an error message, and the HTTP body that was received in
      the request.
  """

  _path = '/api/v1/payment_orders'

  #checks for possible query parameters 
  if date_from and date_to is None:
    _path = _path + f'?from={date_from}'
  elif date_to and date_from is None:
    _path = _path + f'?to={date_to}'
  elif date_from and date_to:
    _path = _path + f'?from={date_from}&to={date_to}'
  
  _url = base_url + _path

  # execute response 
  _response = requests.get(_url, headers=headers)
  return _response

def create_payment_order(headers, base_url, split_tree_id):
  """Does a POST request to /api/v1/payment_orders. 
          
    Creates a new payment order. 

    Args:
      split_tree_id (object, required): An object including the key: "split_tree_id" and a 
      value: with a valid split tree id in String. 
         
    Returns:
      Response: An object with the response value as well as other
      useful information such as status codes and headers.  

    Raises:
      APIException: When an error occurs while fetching the data from
      the remote API. This exception includes the HTTP Response
      code, an error message, and the HTTP body that was received in
      the request.
  """
  
  _path = '/api/v1/payment_orders'
  _url = base_url + _path

  # execute response 
  _response = requests.post(_url, headers=headers, json=split_tree_id)
  return _response

def get_payment_order(headers, base_url, payment_order_id):
  """Does a GET request to /api/v1/payment_orders. 
          
    Retrives a specific payment order. 

    Args:
      payment_order_id (String, required): The ID of the of the payment order to retrive. 
         
    Returns:
      Response: An object with the response value as well as other
      useful information such as status codes and headers.  

    Raises:
      APIException: When an error occurs while fetching the data from
      the remote API. This exception includes the HTTP Response
      code, an error message, and the HTTP body that was received in
      the request.
  """
  _path = f'/api/v1/payment_orders/{payment_order_id}'
  _url = base_url + _path

  # execute response 
  _response = requests.get(_url, headers=headers)
  return _response 

def update_payment_order(headers, base_url, payment_order_id, split_tree_id):
  
  _path = f'/api/v1/payment_orders/{payment_order_id}/update'
  _url = base_url + _path
  _payload = {
    "split_tree_id": split_tree_id
  }

  # execute response 
  _response = requests.put(_url, headers=headers, json=_payload)
  return _response  

def close_payment_order(headers, base_url, payment_order_id):

  _path = f'/api/v1/payment_orders/{payment_order_id}/close'
  _url = base_url + _path
  
  # execute response 
  _response = requests.put(_url, headers=headers)
  return _response  
 

def settle_payment_order(headers, base_url):
  pass 

def split_payment_order(headers, base_url):
  pass 