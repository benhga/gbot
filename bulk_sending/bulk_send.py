# works with both python 2 and 3
from __future__ import print_function

import os
from datetime import datetime

import pandas as pd
from gresponses2 import numbers_list, num_l
from template_send import send_invite

import africastalking


class SMS:

    def __init__(self):
        # Set your app credentials
        self.username = "ASIS038"
        self.api_key = "27977c5e42f686f7e2097b296f42ca041a2bd45bed94489ee3ef1c0d11779ae3"

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self):
        # Set the numbers you want to send to in international format
        # recipients = ["+27833888281", "+27780730005", "+27618129719"]

        # 827245713
        # nums = numbers_list
        nums = num_l
        # num_l = nums["WAB"].values.tolist()

        cleaned = []
        for i in nums:
            i = str(i)
            i = '+' + i
            cleaned.append(i)

        recipients = cleaned
        # recipients = nums
        # print(recipients)
        # print(len(recipients))

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
        month = ((int(datetime.now().year) - 2022) * 12) + (int(datetime.now().month) - 8)

        for row in rows:
            print(row)
            count += 1
                # send_invite(row[1], name)

        print(count)

        # Set your message
        message = "Hi! You have opted into the WageWise survey brought to you by Genesis Analytics. We understand that you have been having issues receiving your R17 airtime for completing the survey. Please follow this simple two step process for us to verify your phone number and get your airtime to you. To get started, just respond to this message.";

        # for num in recipients:
            # send_invite(num, None)



        # print(recipients)
        # Set your shortCode or senderId
        # sender = "GENESIS"
        # try:
        #     # Thats it, hit send and we'll take care of the rest.
        #     response = self.sms.send(message, recipients, sender)
        #     print(response)
        # except Exception as e:
        #     print('Encountered an error while sending: %s' % str(e))


if __name__ == '__main__':
    SMS().send()
