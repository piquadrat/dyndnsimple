#!/usr/bin/env python
import json
import requests
from requests.exceptions import ConnectionError


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


def main():
    import argparse
    PARSER = argparse.ArgumentParser(description='')
    PARSER.add_argument('--email', action="store", dest="email", type=str)
    PARSER.add_argument('--token', action="store", dest="token", type=str)
    PARSER.add_argument('--record_id', action="store", dest="record_id",
                        type=str)
    PARSER.add_argument('--domain_id', action="store", dest="domain_id",
                        type=str)
    PARSER.add_argument('--domain', action="store", dest="domain",
                        type=str)
    options = PARSER.parse_args()

    print "Getting IP..."
    try:
        ip_address = get_ip()
        print "OK: {}".format(ip_address)
        if ip_address:
            print "Updating DNSimple..."
            url = "https://dnsimple.com/domains/{0}/records/{1}"\
                  .format(options.domain_id, options.record_id)
            update_dns(ip_address, url, options)
            print "Done."
    except ConnectionError, e:
        print "Cannot find wan ip: {}".format(e)


if __name__ == '__main__':
    main()
