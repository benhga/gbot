import os

import africastalking
import pandas as pd
import numpy as np

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



def send_many_retrospective():
    # nums = pd.read_csv(os.path.join("glogic", "ASISA Phone numbers 15Aug22.csv"))
    # nums = nums.dropna()
    # nums["Status"] = nums["Status"].map({"Success": 1, "Failed": 0})
    # nums = nums[nums["Status"]==0]
    # nums = nums.drop_duplicates(subset="Recipient", keep="first")
    # nums = nums.reset_index()

    nums = ['+27632691416',
 '+27610865588',
 '+27731207995',
 '+27733802551',
 '+27833256344',
 '+27784746981',
 '+27784488827',
 '+27655866539',
 '+27834010777',
 '+27782835713',
 '+27733213562',
 '+27633321623',
 '+27736121790',
 '+27735778866',
 '+27631877779',
 '+27735555724',
 '+27734757860',
 '+27735838248',
 '+27787638099',
 '+27717601283',
 '+27781673314',
 '+27789336339',
 '+27810798704',
 '+27633143551',
 '+27782564652',
 '+27836176807',
 '+27810926595',
 '+27738235846',
 '+27781421921',
 '+27789094316',
 '+27783001790',
 '+27719981107',
 '+27710230310',
 '+27835407488',
 '+27787330119',
 '+27738703689',
 '+27836871946',
 '+27837812647',
 '+27730077309',
 '+27789086187',
 '+27732356132',
 '+27787118276',
 '+27635729201',
 '+27732253381',
 '+27733447859',
 '+27633995028',
 '+27787235347',
 '+27760146651',
 '+27785819316',
 '+27656495852',
 '+27735770665',
 '+27786315682',
 '+27734481623',
 '+27784989928',
 '+27734541856',
 '+27788444405',
 '+27834978345',
 '+27737398576',
 '+27739360184',
 '+27733660298',
 '+27833742529',
 '+27746189624',
 '+27784114355',
 '+27787752918',
 '+27833396840',
 '+27783605360',
 '+27783522524',
 '+27633418757',
 '+27733806911',
 '+27719634939',
 '+27734480812',
 '+27606290902',
 '+27785371948',
 '+27640360857',
 '+27785879229',
 '+27786348753',
 '+27717794948',
 '+27786168415',
 '+27730418769',
 '+27739829962',
 '+27731934156',
 '+27835976797',
 '+27785591221',
 '+27835705356',
 '+27604828286',
 '+27634151695',
 '+27788116564',
 '+27634981524',
 '+27783874583',
 '+27603386214',
 '+27739766286',
 '+27826799212',
 '+27730336288',
 '+27632290771',
 '+27787083529',
 '+27797922889',
 '+27731262586',
 '+27719236694',
 '+27719879789',
 '+27603637520']
    print(nums)
    print(len(nums))

    # nums_l = []
    # for i in nums:
    #     i = "+" + i
    #     nums_l.append(i)
    # print(nums_l)
    # print(len(nums_l))
    # nums = nums.astype(str)
    # nums['Phone Number'] = nums['Phone Number'].apply(lambda x: "+" + x)
    # num_l = nums["Phone Number"].values.tolist()
    #
    # print(num_l)
    # print(len(num_l))
    for i in nums:
        send_airtime_after_survey(i, 17)


if __name__ == "__main__":
    # multiple_send()
    send_many_retrospective()