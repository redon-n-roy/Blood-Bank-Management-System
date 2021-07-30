import random
from twilio.rest import Client 
import credentials as cred
 
client = Client(cred.login['account_sid'], cred.login['auth_token']) 

def send_otp(otp,mobl):
    message = client.messages.create(  
                                messaging_service_sid=cred.login['messaging_service_sid'], 
                                body='Your OTP for Blood Bank app is '+str(otp),      
                                to=mobl 
                            ) 
    if(message.status == 'accepted'):
        return True
    else:
        return False


def verify_phone(mobile=cred.login['default_number']):
    otpNo = random.randint(1001,9999)
    if(send_otp(otpNo,mobile)):
        print('An OTP has been send to your number.')
        max_attempt =1
        while(max_attempt <=3):
            OTPinp = int(input('Enter the OTP:- '))
            if(OTPinp == otpNo):
                return True
            else:
                print("OTP invalid!")
                max_attempt += 1
        else:
            print("OTP verification failed!")
            return False
    else:
        print("Unable to send sms!")
        return False