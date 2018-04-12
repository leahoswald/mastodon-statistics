#!/usr/bin/env python

import dns.resolver
import requests

data= requests.get("https://chaos.social/api/v1/instance/peers").json()

ipv6 = 0
no4a = 0
nxdomain = 0
broken = 0
dnstimeout = 0

print("Start scanning " + str(len(data)) + " elements")

resolver = dns.resolver.Resolver()
resolver.timeout = 5
resolver.lifetime = 1

for instance in data:
    try:
        answer = resolver.query(instance, "AAAA")
        ipv6 += 1
        print(answer[0])
    except dns.resolver.NoAnswer:
        no4a += 1
        print("No AAAA")
    except dns.resolver.NXDOMAIN:
        nxdomain += 1
        print("No such domain")
    except dns.resolver.NoNameservers:
        broken += 1
        print("DNS ist broken")
    except dns.exception.Timeout:
        dnstimeout += 1
        print("DNS timeout")

print("\ntotal: " + str(len(data)) + "\nIPv6 enabled: " + str(ipv6) + "\nNo AAAA record: " + str(no4a) + "\nNXDOMAIN: " + str(nxdomain) + "\nBroken Nameservers: " + str(broken) + "\nDNS Timeout: " + str(dnstimeout))
