import os

import africastalking
import pandas as pd

def multiple_send():
    # nums = pd.read_csv("Airtime 29+30.xlsx - Sheet1.csv")
    nums = None
    print(len(nums))
    for i in nums['Phone Numbers']:
        num = "+" + str(i)
        send_airtime_after_survey(num)



def send_airtime_after_survey(num, amt=5):
    # username = os.environ.get("AT_USERNAME")
    # api_key = os.environ.get("AT_API_KEY")
    username = "ASIS038"
    api_key = "27977c5e42f686f7e2097b296f42ca041a2bd45bed94489ee3ef1c0d11779ae3"
    africastalking.initialize(username, api_key)

    airtime = africastalking.Airtime

    phone_number = num
    currency_code = "ZAR"  # Change this to your country's code
    amount = amt

    try:
        response = airtime.send(phone_number=phone_number, amount=amount, currency_code=currency_code)
        print('*'*20)
        print(f"Airtime sent to {num}")
        print(response)
        return 1
    except Exception as e:
        print(f"Encountered an error while sending airtime. More error details below\n {e}")
        return -1

if __name__ == "__main__":
    multiple_send()