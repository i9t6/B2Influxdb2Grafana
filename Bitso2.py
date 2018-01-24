#!/usr/bin/env python

import requests
import json
import influxdb

url1 = "https://api.bitso.com/v3/ticker/?book=btc_mxn"
url2 = "https://api.bitso.com/v3/ticker/?book=eth_mxn"
url3 = "https://api.bitso.com/v3/ticker/?book=xrp_mxn"

influx_ip = "127.0.0.1"

data1 = requests.get(url1)
tabla1 = data1.json()

data2 = requests.get(url2)
tabla2 = data2.json()

data3 = requests.get(url3)
tabla3 = data3.json()

#print( json.dumps(data.json(), indent=4, separators=(",",":")))


low1 = tabla1["payload"]["low"]
low2 = tabla2["payload"]["low"]
low3 = tabla3["payload"]["low"]

high1 = tabla1["payload"]["high"]
high2 = tabla2["payload"]["high"]
high3 = tabla3["payload"]["high"]

last1 = tabla1["payload"]["last"]
last2 = tabla2["payload"]["last"]
last3 = tabla3["payload"]["last"]

#fecha = tabla1["payload"]["created_at"].split("T",1)
#dia = fecha[0]
#hora = fecha[1].split("+",1)[0]

db = influxdb.InfluxDBClient(influx_ip, 8086, "paco", "paco", "example")
data1 = [{"measurement":"Crypto-BTC","fields":{"Alto":float(high1),"Bajo":float(low1),"Actual":float(last1)}}]

data2 = [{"measurement":"Crypto-ETH","fields":{"Alto":float(high2),"Bajo":float(low2),"Actual":float(last2)}}]

data3 = [{"measurement":"Crypto-XRP","fields":{"Alto":float(high3),"Bajo":float(low3),"Actual":float(last3)}}]

db.write_points(data1)

db.write_points(data2)

db.write_points(data3)
