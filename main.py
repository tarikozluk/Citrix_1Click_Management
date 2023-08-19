from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
import requests
import json
import time
from flask_cors import CORS
import dns_implementer
from flask_httpauth import HTTPBasicAuth

load_dotenv()
app = Flask(__name__)
auth = HTTPBasicAuth()
cors = CORS(app)

VALID_CREDENTIALS = {
    os.getenv("ROOT_USER"): os.getenv("ROOT_PASS"),
    os.getenv("GUEST_PASS"): os.getenv("GUEST_PASS")
}

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    if request.path == '/':
        if username in VALID_CREDENTIALS and password == VALID_CREDENTIALS[username]:
            return True
        return False
    else:
        return True

@app.route('/', methods=['GET'])
def main_LB_management():

    return render_template('main.html')

@app.route('/hidden_ip', methods=['GET'])
def get_hidden_ip():
    dns_name = request.args.get('dns_name')
    ip_address = dns_implementer.send_ping(message=dns_name)
    return ip_address

if __name__ == '__main__':
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"))
