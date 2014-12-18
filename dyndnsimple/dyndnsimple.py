import json
import requests


def get_ip():
    """ Gets IP address from http://josnip.com """
    response = requests.get("http://jsonip.com")
    return json.loads(response.content).get("ip", None)


class API(object):
    def __init__(self, email, token):
        self.email = email
        self.token = token

    def call(self, url, data=None, method=requests.get):
        if data is None:
            data = {}
        headers = {
            "Content-Type": "application/json",
            "X-DNSimple-Token": "{0}:{1}".format(self.email, self.token),
            "Accept": "application/json",
        }
        response = method(url, data=json.dumps(data), headers=headers)
        return json.loads(response.content)

    def update_dns(self, ip_address, domain, record_id):
        """ Updated DNS Record with new ip address """
        record_url = 'https://api.dnsimple.com/v1/domains/{}/records/{}'.format(
            domain, record_id
        )
        record = self.call(record_url)['record']
        data = {"record": {"name": record['name'], "content": ip_address}}
        response = self.call(record_url, data, method=requests.put)

