import freeclimb
from freeclimb.api import default_api
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()
account_id = os.environ.get("ACCOUNT_ID")
api_key = os.environ.get("API_KEY")
api_server = os.environ.get("API_SERVER", "https://www.freeclimb.com/apiserver")
from_number = os.environ.get("FREECLIMB_NUMBER")

if not account_id or not api_key or not from_number:
    print("ERROR: ENVIRONMENT VARIABLES ARE NOT SET. PLEASE SET ALL ENVIRONMMENT VARIABLES AND RETRY.")
    quit()

app = Flask(__name__)

configuration = freeclimb.Configuration(
    host=api_server,
    username=account_id,
    password=api_key
)

api_client = freeclimb.ApiClient(configuration)
api_instance = default_api.DefaultApi(api_client)

# Specify this route with 'SMS URL' in App Config
@app.route('/incomingSms', methods=['POST'])
def incomingSms():
    if request.method == 'POST':
        message = "Hello, World!"
        _from = from_number #Your FreeClimb Number
        to = request.json['from']
        message_request = freeclimb.MessageRequest(_from=_from, text=message, to=to)
        api_instance.send_an_sms_message(message_request)
        return jsonify({'success':True}), 200, {'ContentType':'application/json'} 

# Specify this route with 'STATUS CALLBACK URL' in App Config
@app.route('/status', methods=['POST'])
def status():
    return jsonify({'success':True}), 200, {'ContentType':'application/json'} 


def quickstart_tutorial():
    obfuscated_api_key = '*'*(len(api_key) - 4)+api_key[-4:]

    print("\nWelcome to FreeClimb!\n")
    print("Your account id: {0}".format(account_id))
    print("Your api key is: {0}\n".format(obfuscated_api_key))
    print("Your web server is listening at: http://127.0.0.1:3000")
    print("Your NEXT STEP is to use NGROK to proxy HTTP Traffic to this local web server.")
    print("\t1. In NGROK, configure the dynamic url to proxy to http://127.0.0.1:3000")
    print("\t2. In the Dashboard or API, set your FreeClimb Application Voice Url to the dynamic endpoint NGROK generated.\n")
    print(api_server)


if __name__ == '__main__':
    quickstart_tutorial()
    app.run(host='0.0.0.0', port=3000)