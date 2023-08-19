from pythonping import ping
import LoadBalancer_Status


def send_ping(message):
    try:
        ping_adress = message
        ping_response = ping(str(ping_adress), verbose=False, count=1, size=1, interval=1,timeout=10)
        ping_text = str(ping_response)
        start_index = ping_text.find("from ") + len("from ")
        end_index = ping_text.find(",", start_index)
        ip_address = ping_text[start_index:end_index]
        servers = LoadBalancer_Status.lb_name_finder(lb_regex=ip_address)
        return servers
    except Exception as e:
        print(e)
        return e

