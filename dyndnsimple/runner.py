#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from .dyndnsimple import get_ip, API
from requests.exceptions import ConnectionError


def run():
    import argparse
    PARSER = argparse.ArgumentParser(description='')
    PARSER.add_argument('--email', action="store", dest="email", type=str,
                        required=True)
    PARSER.add_argument('--token', action="store", dest="token", type=str,
                        required=True)
    PARSER.add_argument('--record_id', action="store", dest="record_id",
                        type=str, required=False)
    PARSER.add_argument('--domain', action="store", dest="domain",
                        type=str, required=True)
    PARSER.add_argument('--cache_file', action="store", dest="cache_file",
                        type=str, required=False)
    options = PARSER.parse_args()

    api = API(options.email, options.token)
    if not options.record_id:
        print('Available records')
        url = 'https://api.dnsimple.com/v1/domains/{}/records'.format(
            options.domain
        )
        data = api.call(url)
        for record in data:
            print('============ Record ============')
            print(
'''Name:\t\t{name}
Type:\t\t{record_type}
Content:\t{content}
ID:\t\t{id}
'''.format(**record['record']))
        return


    print("Getting IP...")
    try:
        ip_address = get_ip()
        print("OK: {}".format(ip_address))
        if options.cache_file:
            mode = 'r+' if os.path.exists(options.cache_file) else 'w'
            with open(options.cache_file, mode=mode) as f:
                old_ip = f.read().strip() if mode != 'w' else None
                if old_ip == ip_address:
                    print("IP did not change since last run")
                    return
                f.seek(0)
                f.write(ip_address)
        if ip_address:
            print("Updating DNSimple...")
            api.update_dns(ip_address, options.domain, options.record_id)
            print("Done.")
    except ConnectionError as e:
        print("Cannot find wan ip: {}".format(e))
