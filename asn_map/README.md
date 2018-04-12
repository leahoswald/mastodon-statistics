#### Dependencies

* dnspython
* pyasn

#### Usage

To run these scripts you have to download the database files for [pyasn](https://pypi.python.org/pypi/pyasn).
To query the data for IPv4 and IPv6 you have to call:
```
pyasn_util_download.py -46

```
After that you have to convert the data with:
```
pyasn_util_convert.py --single rib<date string>.bz2 asn.db

```
For the ASN to name stuff you need to download the ASN name data:
```
pyasn_util_asnames.py -o asn_names.json

```
and also convert it:
```
pyasn_util_convert.py --single asn_names.json asn_name.db

```
To filter the results by Country count
```
python as-to-country.py | sort | uniq -c | sort -n  

```
To filter the ASN results by ASN count
```
 | sort -n | uniq -c | sort -n | wc -l
```
To filter the ASN names by name count
```
python as-to-name.py | sort | uniq -c | sort -n 
```

#### Data in this repo
This repo also contains my data from a scan at the 10.04.2018 with the instance list from mastodon.social
