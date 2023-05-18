from __future__ import print_function
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.message_request import MessageRequest
import os
import json
from flask import Flask, request

configuration = freeclimb.Configuration(
    username = os.environ['ACCOUNT_ID'],
    password = os.environ['API_KEY']
)

api_client = freeclimb.ApiClient(configuration)
api_instance = default_api.DefaultApi(api_client)

app = Flask(__name__)

# Specify this route with 'SMS URL' in App Config
@app.route('/incomingSms', methods=['POST'])
def incomingSms():
    if request.method == 'POST':
        message = "Hello World!"
        _from = "" #Your FreeClimb Number
        to = request.json['from']
        message_request = MessageRequest(_from=_from, text=message, to=to)
        api_instance.send_an_sms_message(message_request)

        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

# Specify this route with 'STATUS CALLBACK URL' in App Config
@app.route('/status', methods=['POST'])
def status():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

