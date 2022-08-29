import os
from twilio.rest import Client

if __name__ == '__main__':
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
             from_='whatsapp:+27600185052',
             body='Hello, Martina. You opted into the WageWise 3-year survey brought to you by Genesis Analytics. It’s time to complete this month’s survey. Reply Yes to get started and earn your R17 of airtime.',
             to='whatsapp:+447508963162'
         )

    print(message.sid)


