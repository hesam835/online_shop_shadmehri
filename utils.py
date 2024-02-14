from kavenegar import APIException,HTTPException
from kavenegar import KavenegarAPI
from kavenegar import *
def send_otp_code(phone_number,code):
    try:
        api=KavenegarAPI('73664731726E334441346A5234662F444E34487558736E6A72304E6D5A75562F6B6E3259766A752F5A72343D')
        params={'sender' : "",
                'receptor' : phone_number,
                'message' : f"your code{code}"
        } 
        response = api.sms_send(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)
