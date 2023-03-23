#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import date

today = date.today()
Dictionary = {

    "welcome1": "Hello 😀 \n\n\
Genesis Analytics invites you to participate in the ASISA Foundation’s WageWise financial education survey over the next 3-years. Answer questions and earn airtime.\n\n\
Your personal information and responses will not be shared and are only used for research purposes. Your participation will not impact your ability to participate in WageWise or affect your ability to receive future financial or training support. Please see our T&Cs here: shorturl.at/BDPX6\
",
    "welcome2_1": "You earn R17 each month in airtime by answering 3 questions monthly via WhatsApp AND you can earn R75 in airtime by responding to an annual survey.",
    "welcome2":"This will not take up much of your time and you will be rewarded for answering our questions. Once the first survey is completed, you will earn R75 airtime, and you will be registered to complete monthly surveys that will earn you R17 airtime. You will receive messages each month to invite you to complete the monthly survey. _You will not receive any remuneration if you did not pariticipate in the WageWise programme_.",

    "welcome3": "You can opt out at any time by sending *STOP*. To consent to participation and earn your R17 airtime, please send *YES* to continue.",
    "thanks": "\U00002705 Thank you for completing the survey. "
}

survey_questions = {
    "question1": "When you experienced a financial emergency or had an expense that you didn’t plan for, in the last month \
did you…\n\n\
1) Have enough saved to pay for the unexpected expense\n\
2) Take a loan from a bank or from your home loan\n\
3) Borrow money from friends or family\n\
4) Borrow money from a microlender or somewhere else other than a bank\n\
5) Borrow money from a funding source like a stokvel\n\
6) Use a credit card to pay the expense\n\
7) Not pay\n\
8) I did not have a financial emergency in the last month",

    "question2" : "When you faced a financial problem, in the last month did you…\n\n\
1) Refer to the WageWise booklet and tools\n\
2) Refer to the WageWise website for helpful resources\n\
3) Refer to the WageWise Facebook Page\n\
4) Reach out to other WageWise participants\n\
5) Refer to another source of assistance\n\
6) None of the above\
",

    "question3":"In the last month, have you done any of the following (select all that apply)\n\n\
1) Budgeted\n\
2) Opened a savings account to start saving\n\
3) Paid off a debt or credit obligation, e.g., closed a clothing\n\
store account\n\
4) Met your monthly debt repayments\n\
5) Negotiated a better interest rate on your debt\n\
6) Seen a financial advisor\n\
7) Started saving for retirement\n\
8) Shared what I have learned from WageWise with my family and friends\n\
",
    "question4": "How old are you?\n\n\
1. 18-35 years old\n\
2. 36-50 years old\n\
3. 51-64 years old\n\
4. Above 65 years old\n\
",
    "question5" : "Which province do you live in?\n\n\
1. Eastern Cape\n\
2. Free State\n\
3. Gauteng\n\
4. Kwazulu Natal\n\
5. Limpopo\n\
6. Mpumalanga\n\
7. Northern Cape\n\
8. North West\n\
9. Western Cape\n\
",
    "question6": "What is your employment status?\n\n\
1. Employed\n\
2. Employed with a side hustle\n\
3. Self-employed\n\
4. Unemployed\n\
",
    "question7": "What sector are you employed in?\n\n\
1. Public sector\n\
2. Private Sector\n\
3. Community based organisation\n\
4. Unemployed\n\
",

    "question8" : "How much do you earn per WHAT?\n\n\
1. No income\n\
2. Less than R3 000\n\
3. R3 001 - R5 000\n\
4. R5 001 - R8 000\n\
5. R8 001 - R12 000\n\
6. R12 001 - R15 000\n\
7. R15 001 - R20 000 \n\
8. Over R20 000\n\
9. Prefer not to say\n\
",

    "question9": "What sector are you employed in?\n\n\
1. 0-Grade9\n\
2. Grade9-less Matric\n\
3. Completed Matric\n\
4. Post Matric Qualification\n\
",

    "question10":"Do you have a disability?\n\n\
1. Yes\n\
2. No\n\
3. Prefer not to say\n\
",
}

num_l = ["27725437490", "27822205729"]
numbers_list = [
"27782564652",
"27676066880",
"27769047611",
"27797922889",
"27620067904",
"27784695353",
"27787638099",
"27609262149",
"27610865588",
"27635641027",
"27635729201",
"27636032789",
"27640173654",
"27648166807",
"27655866539",
"27665257082",
"27671855312",
"27712164502",
"27717601283",
"27719595581",
"27719990980",
"27727512799",
"27730336288",
"27734480812",
"27735770665",
"27736276520",
"27739360184",
'27739766286',
"27761702479",
"27762784025",
"27780968800",
"27781655357",
"27783522524",
"27784989928",
"27788444405",
"27793531594",
"27796067665",
"27813552191",
"27818788865",
"27823513847",
"27834978345",
"27835976797",
"27836871946",
"27839931950",
"27733447859",
"27632691416",
"27604828286",
"27606290902",
"27633321623",
"27710230310",
"27717794948",
"27720542791",
"27723526260",
"27731207995",
"27731262586",
"27732356132",
"27733660298",
"27733806911",
"27734481623",
"27736121790",
"27737398576",
"27738235846",
"27738703689",
"27746189624",
"27760146651",
"27781673314",
"27783001790",
"27783874583",
"27784746981",
"27785371948",
"27785591221",
"27786315682",
"27787083529",
"27787118276",
"27789336339",
"27826799212",
"27833396840",
"27833742529",
"27835705356",
"27634442157",
"27661592329",
"27710494433",
"27715660036",
"27605759416",
"27618628683",
"27639420504",
"27762189607",
"27825986715",
"27732104151",
"27734054274",
"27739074600",
"27748204021",
"27748250036",
"27786499022",
"27814713730",
"27742394951",
"27614566657",
"27612605938",
"27630685743",
"27732220847",
"27840738480",
"27616046800",
"27619825209",
"27640966060",
"27720362124",
"27720925660",
"27723472053",
"27733656219",
"27785143736",
"27786401124",
"27788216339",
"27795722853",
"27836373831",
"27844381082",
"27737419835",
"27678045433",
"27679058295",
"27681920217",
"27780619941",
"27781713857",
"27793464829",
"27820711954",
"27822566446",
"27603029990",
"27604195350",
"27604317872",
"27606663555",
"27607286292",
"27608746836",
"27610842130",
"27613401770",
"27616272326",
"27619654423",
"27621674469",
"27631140440",
"27634634686",
"27635634618",
"27638687298",
"27639720968",
"27644734458",
"27646093370",
"27646836128",
"27648344741",
"27648579380",
"27648957649",
"27651052175",
"27651389847",
"27652527509",
"27655917789",
"27656118009",
"27656236171",
"27657061237",
"27659270995",
"27663166290",
"27663376422",
"27663670299",
"27665642033",
"27671934572",
"27676810120",
"27679280727",
"27679687240",
"27694765449",
"27695520836",
"27711331094",
"27711432285",
"27711536389",
"27711745875",
"27711875480",
"27713969268",
"27714725147",
"27714836784",
"27715021951",
"27715372005",
"27715957955",
"27717545339",
"27719524236",
"27722964752",
"27723260736",
"27724709681",
"27725179256",
"27728356960",
"27731243325",
"27732466772",
"27733187036",
"27734584714",
"27734651088",
"27736250009",
"27736280425",
"27736513032",
"27738845544",
"27742353934",
"27747825128",
"27749696291",
"27760755160",
"27761254597",
"27762096653",
"27762284079",
"27762593272",
"27764349433",
"27764877778",
"27765660570",
"27766561208",
"27767349637",
"27767915889",
"27768958336",
"27783027111",
"27785310907",
"27786976805",
"27787007814",
"27787844423",
"27788800272",
"27790507013",
"27793720199",
"27794611658",
"27794635360",
"27794805670",
"27797353823",
"27798176307",
"27799286579",
"27810883227",
"27812078802",
"27813032658",
"27815047027",
"27815736423",
"27815737151",
"27818824457",
"27823068051",
"27827292546",
"27834113087",
"27835306090",
"27836566421",
"27837973929",
"27849190082"
]
