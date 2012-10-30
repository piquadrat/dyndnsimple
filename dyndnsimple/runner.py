#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .dyndnsimple import get_ip, update_dns
from requests.exceptions import ConnectionError


def run():
    import argparse
    PARSER = argparse.ArgumentParser(description='')
    PARSER.add_argument('--email', action="store", dest="email", type=str,
                        required=True)
    PARSER.add_argument('--token', action="store", dest="token", type=str,
                        required=True)
    PARSER.add_argument('--record_id', action="store", dest="record_id",
                        type=str, required=True)
    PARSER.add_argument('--domain_id', action="store", dest="domain_id",
                        type=str, required=True)
    PARSER.add_argument('--domain', action="store", dest="domain",
                        type=str, required=True)
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
