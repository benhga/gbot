import os
from twilio.rest import Client
import pyodbc
from sql_stuff import get_data_ud

def send_invite(num, name):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        from_='whatsapp:+27600185052',
        body=f'Hello again, {name}. I see you haven’t completed the survey this month yet although you have requested to receive surveys as part of the WageWise 3 year survey. Would you like to get started now? Reply *Yes* to get started and earn your R17 of airtime.',
        to=f'whatsapp:{num}'
    )

    print(message.sid)

if __name__ == '__main__':
    server = os.environ.get('SERVER')
    database = os.environ.get('DATABASE')
    username = os.environ.get('NAME')
    password = os.environ.get('PASSWORD')

    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM users")

    rows = cursor.fetchall()
    count = 0
    for row in rows:
        if int(row[3]) == 1 and int(row[4]) == 0:
            print(row)
            print(f"Number: {row[1]}. Registered: {row[3]}. Last Month: {row[4]}")
            namel = get_data_ud(row[1], cursor)
            namel = namel.split(" ")
            name = namel[0]
            name = name[0].upper() + name[1:].lower()
            count+=1
            send_invite(row[1], name)

    print(count)
    # send_invite("+27822205729", "Ben")

