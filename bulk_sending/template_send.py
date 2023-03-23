import os
from datetime import datetime

from twilio.rest import Client
import pyodbc

def send_invite(num, name):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        from_='whatsapp:+27600185052',
        body="Hi! You have opted into the WageWise survey brought to you by Genesis Analytics. We understand that you have been having issues receiving your R17 airtime for completing the survey. Please follow this simple two step process for us to verify your phone number and get your airtime to you. To get started, just respond to this message. ",
        to=f'whatsapp:{num}'
    )

    print(message.sid)

def delete_user_from_airtime_list(num):
    server = os.environ.get('SERVER')
    database = os.environ.get('DATABASE')
    username = os.environ.get('NAME')
    password = os.environ.get('PASSWORD')

    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM airtime_correction_numbers WHERE number={num}")
    conn.commit()
    # row = cursor.fetchone()
    # print(row)

def check_user_in_airtime_list(num):
    server = os.environ.get('SERVER')
    database = os.environ.get('DATABASE')
    username = os.environ.get('NAME')
    password = os.environ.get('PASSWORD')

    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM airtime_correction_numbers WHERE number={num}")

    row = cursor.fetchone()
    if row:
        return True

    return False



if __name__ == '__main__':
    server = os.environ.get('SERVER')
    database = os.environ.get('DATABASE')
    username = os.environ.get('NAME')
    password = os.environ.get('PASSWORD')

    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM airtime_correction_numbers")

    rows = cursor.fetchall()
    count = 0
    month=((int(datetime.now().year) - 2022)*12) +  (int(datetime.now().month) - 8)


    for row in rows:
        print(row[1])
        # print(f"Number: {row[1]}. Registered: {row[3]}. Last Month: {row[4]}")
        # namel = get_data_ud(row[1], cursor)
        # namel = namel.split(" ")
        # name = namel[0]
        # name = name[0].upper() + name[1:].lower()
        count+=1
            # send_invite(row[1], name)

    print(count)
    send_invite("+27725437490", "Ben")



