import pyasn

asndb = pyasn.pyasn('asn.db', 'asn_names.json')

with open("mastodon.asn.list", 'r') as f:
    for asn in f:
        try:
            print(asndb.get_as_name(int(asn)).split(',', 1)[0])
        except:
            pass
