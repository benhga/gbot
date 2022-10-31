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

    nums = ["27839931950",
"27734480812",
"27733660298",
"27717794948",
"27679280727",
"27815047027",
"27728356960",
"27619654423",
"27679058295",
"27797353823",
"27794635360",
"27604828286",
"27648579380",
"27711536389",
"27794805670",
"27823513847",
"27646836128",
"27749696291",
"27749696291",
"27656236171",
"27733806911",
"27785143736",
"27785591221",
"27786976805",
"27810883227",
"27794611658",
"27676108951",
"27604317872",
"27783874583",
"27833396840",
"27633321623",
"27633321623",
"27764349433",
"27711432285",
"27657061237",
"27711331094",
"27793531594",
"27736276520",
"27835306090",
"27731207995",
"27613401770",
"27676810120",
"27646093370",
"27715021951",
"27720925660",
"27791200680",
"27673154558",
"27847329457",
"27717722439",
"27810798704",
"27813194537",
"27769047611",
"27646184923",
"27782666657",
"27789094316",
"27617394594",
"27641899241",
"27764621474",
"27739360184",
"27660409933",
"27787752918",
"27730762510",
"27639106725",
"27834947112",
"27718473480",
"27727520373",
"27637717052",
"27788285842",
"27788285842",
"27782157372",
"27641270826",
"27658194726",
"27712836178",
"27637353934",
"27732681568",
"27717601283",
"27769341132",
"27781421921",
"27720696539",
"27836373831",
"27733802551",
"27791125778",
"27829566072",
"27760869461",
"27719634939",
"27786168415",
"27723938151",
"27825985649",
"27719981107",
"27710806700",
"27693761307",
"27769909537",
"27828361064",
"27791878149",
"27843378515",
"27832444823",
"27764624245",
"27826324642",
"27797922889",
"27610865588",
"27745341052",
"27720180479",
"27796295999",
"27793895769",
"27739806925",
"27637265269",
"27782564652",
"27814178026",
"27749189624",
"27719879789",
"27839740605",
"27634981524",
"27817431915",
"27820773492",
"27638541982",
"27607986811",
"27735416653",
"27725556566",
"27713317804",
"27783605360",
"27825185845",
"27849780913",
"27677216666",
"27787638099",
"27823738985",
"27725299023",
"27715236051",
"27846114599",
"27827438495",
"27782835713",
"27710640339",
"27789086187",
"27660687243",
"27783522524",
"27764146028"]

    nums_l = []
    for i in nums:
        i = "+" + i
        nums_l.append(i)
    print(nums_l)
    print(len(nums_l))
    # nums = nums.astype(str)
    # nums['Phone Number'] = nums['Phone Number'].apply(lambda x: "+" + x)
    # num_l = nums["Phone Number"].values.tolist()
    #
    # print(num_l)
    # print(len(num_l))
    for i in nums_l:
        send_airtime_after_survey(i, 17)


if __name__ == "__main__":
    # multiple_send()
    send_many_retrospective()