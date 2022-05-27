import os

import africastalking


def send_airtime_after_survey(num):
    username = os.environ.get("AT_USERNAME")
    api_key = os.environ.get("AT_API_KEY")

    africastalking.initialize(username, api_key)

    airtime = africastalking.Airtime

    phone_number = num
    currency_code = "ZAR"  # Change this to your country's code
    amount = 5

    try:
        response = airtime.send(phone_number=phone_number, amount=amount, currency_code=currency_code)
        print(response)
        return 1
    except Exception as e:
        print(f"Encountered an error while sending airtime. More error details below\n {e}")
        return -1
