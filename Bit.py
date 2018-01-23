#!/usr/bin/env python

import requests
import json
url = "https://api.bitso.com/v3/ticker/?book=xrp_mxn"

data = requests.get(url)
tabla = data.json()

print( json.dumps(data.json(), indent=4, separators=(",",":")))
tabla = data.json()

low = tabla["payload"]["low"]
#print low

high = tabla["payload"]["high"]
#print high

last = tabla["payload"]["last"]
#print last

fecha = tabla["payload"]["created_at"].split("T",1)
dia = fecha[0]
hora = fecha[1].split("+",1)[0]
#print time


file = open('bitso.txt', 'w')


file.write("highest:"+high+"\t"+"dia:"+dia+"\t"+"hora:"+hora+"\n")
file.write("lowest:"+low+"\t"+"dia:"+dia+"\t"+"hora:"+hora+"\n")
file.close()
