#!/usr/bin/env python

import dns.resolver
import requests

data= requests.get("https://mastodon.social/api/v1/instance/peers").json()

ipv6 = 0
no4a = 0
no = 0
hbi = 0

print("Start scanning " + str(len(data)) + " elements")

for instance in data:
    try:
        answer = dns.resolver.query(instance, "AAAA")
        print(answer[0])
    except dns.resolver.NoAnswer:
        try:
            answer = dns.resolver.query(instance, "A")
            print(answer[0])
        except:
            continue
    except:
        continue
