import requests
from ping.helper.apiResponse import ApiResponse
from ping.helper.apiHelper import json_deserialize


def get_merchants(headers, base_url):
    """Does a GET request to /api/v1/merchants. 
        
    Lists merchants associated with a tenant. The merchant details
    include email, id, name, organization number and phone number. 

    Args:
        None arguments.  

    Returns:
        Response: An object with the response value as well as other
        useful information such as status codes and headers.  

    Raises:
        APIException: When an error occurs while fetching the data from
        the remote API. This exception includes the HTTP Response
        code, an error message, and the HTTP body that was received in
        the request.
    """

    #Prepare and execute response
    _path = '/api/v1/merchants'
    _url = base_url + _path
    _response = requests.get(_url, headers=headers)

    #deserialize 
    decoded = json_deserialize(_response.text)
    if type(decoded) is dict:
        _errors = decoded.get('errors')
    else:
        _errors = None
    _result = ApiResponse(_response, body=decoded, errors=_errors)
    return _result

def create_new_merchant(headers, base_url, object):
    """Does a POST request to /api/v1/merchants. 
    
    Creates a new merchants for a tenant. 
    You must provide a object with the following values:
    - "name"
    - "organization_number"

    Args:
        Body: An object containing the fields to
        POST for the request.  

    Returns:
        Response: An object with the response value as well as other
        useful information such as status codes and headers.  

    Raises:
        APIException: When an error occurs while fetching the data from
        the remote API. This exception includes the HTTP Response
        code, an error message, and the HTTP body that was received in
        the request.
    """

    #Prepare and execute response 
    _path = '/api/v1/merchants'
    _url = base_url + _path
    _response = requests.post(_url, headers=headers, json=object)

    #deserialize 
    decoded = json_deserialize(_response.text)
    if type(decoded) is dict:
        _errors = decoded.get('errors')
    else:
        _errors = None
    _result = ApiResponse(_response, body=decoded, errors=_errors)
    return _result

def get_specific_merchant(headers, base_url, merchant_id):
    """Does a GET request to /api/v1/merchants/{merchant_id}. 
    
    Provides details for a single merchant. The details include email, id,
    name, organization name, organization number, phone number and status.

    Args:
        merchant_id (string). The ID of the of the merchant to retrive. 

    Returns:
        Response: An object with the response value as well as other
        useful information such as status codes and headers.  

    Raises:
        APIException: When an error occurs while fetching the data from
        the remote API. This exception includes the HTTP Response
        code, an error message, and the HTTP body that was received in
        the request.
    """

     #Prepare and execute response 
    _path = f'/api/v1/merchants/{merchant_id}'
    _url = base_url + _path
    _response = requests.get(_url, headers=headers)

    #deserialize 
    decoded = json_deserialize(_response.text)
    if type(decoded) is dict:
        _errors = decoded.get('errors')
    else:
        _errors = None
    _result = ApiResponse(_response, body=decoded, errors=_errors)
    return _result

