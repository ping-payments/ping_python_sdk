import jsonpickle
from ping.helper.apiResponse import ApiResponse

def json_deserialize(json, unboxing_function=None, as_dict=False):
    """JSON Deserialization of a given string.
    Args:
        json (str): The JSON serialized string to deserialize.
    Returns:
        dict: A dictionary representing the data contained in the
            JSON serialized string.
    """
    if json is None:
        return None

    try:
        decoded = jsonpickle.decode(json)
    except ValueError:
        return json

    if unboxing_function is None:
        return decoded

    if as_dict:
        return {k: unboxing_function(v) for k, v in decoded.items()}
    elif type(decoded, list):
        return [unboxing_function(element) for element in decoded]
    else:
        return unboxing_function(decoded)


def check_errors(response, decoded):
    if type(decoded) is dict:
        errors = decoded.get('errors')
    else:
        errors = None
    result = ApiResponse(response, body=decoded, errors=errors)
    return result


def get_base_url(environment):
    base_url = "http://sandbox.pingpayments.com/payments"
    
    if environment == "sandbox":
        base_url = "http://sandbox.pingpayments.com/payments"
    elif environment == "production":
        base_url = "http://pingpayments.com/payments"
            
    return base_url  

