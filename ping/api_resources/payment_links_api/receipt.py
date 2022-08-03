import requests
from ping.helper.apiHelper import check_errors, json_deserialize

def get(headers, base_url, payment_link_id):
    # Does a GET request to /api/v1/payment_orders/{payment_order_id}.

    # Retrives a specific payment order.
    # Args (provided by the tenant):
    #    payment_order_id (String, required): The ID of the of the payment order to retrive.
    # Returns:
    #    Response: A json object with the response value as well as other
    

    # Prepare and execute response
    _path = f'/api/v1/payment_links/{payment_link_id}/invoice'
    _url = base_url + _path
    response = requests.get(_url, headers=headers)

    # deserialize and check errors
    decoded = json_deserialize(response.text)
    _result = check_errors(response, decoded)
    return _result