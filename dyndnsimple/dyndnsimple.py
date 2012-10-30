import json
import requests


def get_ip():
    """ Gets IP address from http://josnip.com """
    response = requests.get("http://jsonip.com")
    return json.loads(response.content).get("ip", None)


def update_dns(ip_address, url, options):
    """ Updated DNS Record with new ip address """
    data = {"record": {"name": "h", "content": ip_address}}
    headers = {"Content-Type": "application/json",
               "X-DNSimple-Token": "{0}:{1}"
               .format(options.email, options.token),
               "Accept": "application/json"}
    response = requests.put(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 200
