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
        nums = pd.read_excel("glogic/not_interacted.xlsx")

        nums = ["+27614566657",
                "+27742394951",
                "+27748204021",
                "+27734054274",
                "+27814713730",
                "+27748250036",
                "+27732104151",
                "+27739074600",
                "+27786499022",
                "+27762189607",
                "+27639420504",
                "+27618628683",
                "+27605759416",
                "+27825986715",
                "+27712164502",
                "+27715660036",
                "+27789336339",
                "+27632691416",
                "+27782334768",
                "+27738268596",
                "+27710494433",
                "+27661592329",
                "+27634442157"]

        # num_l = nums["WAB"].values.tolist()

        # cleaned = []
        # for i in num_l:
        #     i = str(i)
        #     i = '+' + i
        #     cleaned.append(i)

        # recipients = cleaned
        recipients = nums
        print(recipients)
        print(len(recipients))

        # Set your message
        message = "There’s still time to participate in the WageWise survey and earn R75 airtime. Click and send “Hi” https://wa.me/27600185052?text=Hi";

        # print(recipients)
        # Set your shortCode or senderId
        sender = "GENESIS"
        try:
            # Thats it, hit send and we'll take care of the rest.
            response = self.sms.send(message, recipients, sender)
            print(response)
        except Exception as e:
            print('Encountered an error while sending: %s' % str(e))


if __name__ == '__main__':
    SMS().send()
