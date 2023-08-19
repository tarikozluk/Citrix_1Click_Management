#todo: server listing will be embedded here
import requests
import os
from dotenv import load_dotenv

load_dotenv()
user = os.getenv("CITRIX_USER")
password = os.getenv("CITRIX_PASSWORD")
def NS_Lister(correct_LB):
    app_name = correct_LB
    ###nitro/v1/config/lbvserver_servicegroupmember_binding/deneme

    try:
        for i in range(1, 3):
            url = 'https://' + os.getenv("CITRIX_URL_{}".format(str(i))) + '/nitro/v1/config/lbvserver_servicegroupmember_binding/' + app_name
            response = requests.get(url, auth=(user, password), verify=False)
            data = response.json()
            server_lists = []
            for i in range(len(data['lbvserver_servicegroupmember_binding'])):
                server_lists.append(data['lbvserver_servicegroupmember_binding'][i]['ipv46'])
            server_lists_text = ", ".join(server_lists)
            return server_lists_text
    except Exception as e:
        print("zort")
        return e
