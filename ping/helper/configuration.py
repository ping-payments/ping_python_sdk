
def get_base_url(environment):
    base_url = "http://sandbox.pingpayments.com/payments"
    
    if environment == "sandbox":
        base_url = "http://sandbox.pingpayments.com/payments"
    elif environment == "production":
        base_url = "http://pingpayments.com/payments"
            
    return base_url  

