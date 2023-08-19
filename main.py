from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
import requests
import json
import time
from flask_cors import CORS
import dns_implementer

load_dotenv()
app = Flask(__name__)
cors = CORS(app)
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
