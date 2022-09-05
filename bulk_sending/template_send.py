import os
from twilio.rest import Client
import pandas as pd

def send_invite(num, name):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        from_='whatsapp:+27600185052',
        body=f'Hello, {name}. You opted into the WageWise 3-year survey brought to you by Genesis Analytics. It’s time to complete this month’s survey. Reply Yes to get started and earn your R17 of airtime.',
        to=f'whatsapp:{num}'
    )

    print(message.sid)

if __name__ == '__main__':

    df = pd.read_excel('./Monthly User Database.xlsx', sheet_name='Test 20')

    sendees = {}
    nums = df['Phone_Number_1'].values.tolist()
    names = df['First_Name'].values.tolist()

    for i in range(len(nums)):
        sendees[names[i]] = "+" + str(nums[i])

    sendees["Ben"] = "+27822205729"
    for i in sendees:
        send_invite(sendees[i], i)


