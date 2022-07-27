# works with both python 2 and 3
from __future__ import print_function
import pandas as pd

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
            nums = pd.read_csv("test_nums.csv")

            num_l = nums.numbs.values.tolist()
            cleaned = []
            for i in num_l:
                i = i[1:]
                i = i.replace(" ", "")
                i = i.replace(" ", "")
                i = "+27" + i
                cleaned.append(i)

            recipients = cleaned

            # Set your message
            message = "Genesis invites you to the WageWise WhatsApp study. Earn R75 airtime by answering 15 questions. Click the link and send “Hi” https://wa.me/27600185052?text=Hi";


            # Set your shortCode or senderId
            sender = "GENESIS"
            try:
                # Thats it, hit send and we'll take care of the rest.
                response = self.sms.send(message, recipients, sender)
                print (response)
            except Exception as e:
                print ('Encountered an error while sending: %s' % str(e))

if __name__ == '__main__':
    SMS().send()