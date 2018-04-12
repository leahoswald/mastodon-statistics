import pyasn

asndb = pyasn.pyasn('asn.db')

with open("mastodon.ip.list", 'r') as f:
    for line in f:
        try:
            print(asndb.lookup(line.strip())[0])
        except:
            print("fail -- " + line)
            raise
