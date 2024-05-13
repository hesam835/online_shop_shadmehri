# # import requests
# import json
# from django.conf import settings
# if settings.SANDBOX:
#     sandbox = 'sandbox'
# else:
#     sandbox = 'www'
# ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
# ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
# ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"
# description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
# CallbackURL = 'http://127.0.0.1:8080/order/verify/'

# class ZarinPay():
#     def __init__(self) -> None:
#         pass
    
#     def createpayment(self,amount,authority,isSucess):
#         data = {
#         "MerchantID": settings.MERCHANT,
#         "Amount": amount,
#         "Authority": authority,
#         }
#         data = json.dumps(data)
#         headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
#         # responseString = ["status":"true","RefID":"123456"}'
#         if isSucess == True:
#             return {'status': True, 'RefID':"123456"}
#         else:
#             return {'status': False, 'RefID':"123456"}
#         # response = requests.post(ZP_API_REQUEST, data=data,headers=headers, timeout=10)
#         # if response.status_code == 200:
#         #     response = response.json()
#         #     if response['Status'] == 100:
#         #         return {'status': True, 'RefID': response['RefID']}
#         #     else:
#         #         return {'status': False, 'code': str(response['Status'])}
#         # return response

# payment=ZarinPay()
# amount=payment.createpayment(32)