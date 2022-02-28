
class Configuration():

    def __init__(self,environment):
        self.environment = environment

    def get_base_url(self):
        base_url = "http://sandbox.pingpayments.com/payments"

        if self.environment == "sandbox":
            base_url = "http://sandbox.pingpayments.com/payments"
        elif self.environment == "production":
            base_url = "http://pingpayments.com/payments"
            
        return base_url  

