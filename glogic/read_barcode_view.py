
from . import app, db, bot_view
from flask import url_for, request, session
from .gresponses import Dictionary
from twilio.twiml.messaging_response import MessagingResponse

import requests
from pyzbar import pyzbar
import cv2
from PIL import Image
from io import BytesIO
from .models import Items


@app.route('/read_barcode', methods=['GET', 'POST'])
def read_barcode():
    """
    Redirect for the careers view. Holds careers logic.
    :return str: response
    """
    session['View'] = 'read_barcode'

    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    msg = response.message()

    # print(request.form)
    media_type = request.form.get('MediaContentType0')

    if 'send' in incoming_msg:
        out = Dictionary['send']

    elif ('hi' in incoming_msg) or ('menu' in incoming_msg):
        out = return_to_menu()

    elif 'image' in media_type or 'pdf' in media_type:
        url = request.form.get('MediaUrl0')
        r = requests.get(url, allow_redirects=True)
        # open('barcodes/barcode', 'wb').write(r.content)
        img = Image.open(BytesIO(r.content))
        type, data = decode(img)
        barcode_url = "https://api.barcodelookup.com/v2/products?barcode={data}&key=za1vlihzm8ish3ex57tw1u0wk0per6".format(data=data)
        product = requests.get(barcode_url, allow_redirects=True)
        print(product)
        out = 'should be saved'



    else:
        out = "I'm sorry, I'm still young and don't understand your request. \
    Please use the words in bold to talk to me."

    msg.body(out + "\n\nIf you would like to return to the careers menu, type *careers*.\n\nIf you would like to " +
                   "return the main menu, just say *Hi* or type *Menu*.")

    return str(response)


def return_to_menu():
    """
    Main function is to remove 'View' from session.
    Should probably be put in views/bot_view and imported to each other view.
    :return str: out
    """
    out = Dictionary['hello']
    if 'View' in session:
        del session['View']
    return out

def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        print("detected barcode:", obj)
        # image = draw_barcode(obj, image)
        # print barcode type & data
        type = obj.type
        data = obj.data

        data = data.decode('utf-8')

        print("Type:", obj.type)
        print("Data:", data)

    return type, data


def draw_barcode(decoded, image):
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top),
                            (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                            color=(0, 255, 0),
                            thickness=5)
    return image