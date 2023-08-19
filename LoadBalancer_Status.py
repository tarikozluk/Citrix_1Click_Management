#todo: citrix operations here
import requests
import os
from dotenv import load_dotenv
import List_Servers
from re import search


load_dotenv()
user = os.getenv("CITRIX_USER")
password = os.getenv("CITRIX_PASSWORD")


def lb_name_finder(lb_regex):
    try:
        for i in range(1, 3):
            url = 'https://'+os.getenv("CITRIX_URL_{}".format(str(i)))+'/nitro/v1/config/lbvserver'
            response = requests.get(url, auth=(user, password), verify=False)
            lb_content = response.json()
            for lbs in range(len(lb_content['lbvserver'])):
                if search(lb_regex, lb_content['lbvserver'][lbs]['name']):
                    lb_full_name = lb_content['lbvserver'][lbs]['name']
                    servers_listed = List_Servers.NS_Lister(correct_LB=lb_full_name)
                    return servers_listed
    except:
        print("Nothing to view")