#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import date

Dictionary = {

    # covid related information
    "welcome": "Dear Colleague/Visitor,\n\n\
This screening form is for individuals to complete prior to arrival at the Genesis Analytics office. \
Your phone number will be recorded when you submit this form solely for the purpose of this screening.\
",

    # initial introduction
    "question": "Do you have any symptoms or have had close contact with someone with a flu-like illness or COVID-19 in the last 5 days? \n\
\n\
- any flu like symptoms? \n\
- a fever, sore throat, headache or cough? \n\
- shortness of breath/difficulty breathing? \n\
- chills or muscle pain? Nausea, any vomiting or diarrhea? \n\
- loss of taste or smell?\n\
\n\
Please reply with a single message of *Yes* or *No*.\n\n\
_This screening application has been developed by Genesis Analytics_\
",
    "yes" : f"\U0001F6AB Regrettably, we are unable to offer you access on *{date.today()}* as a result of your answers. \
We recommend you monitor your condition and engage a medical expert. DoH guidance on COVID-19 can be found here (http://health.gov.za/covid19/faq/covid19.html).",

    "no": f"\U00002705 Thank you for completing the clearance. You are clear for access on *{date.today()}*. \
We look forward to seeing you! Please be ready to present this message on arrival.",
}
