#!/usr/bin/env python

import requests
import json
import influxdb

url = "https://api.bitso.com/v3/ticker/?book=xrp_mxn"

data = requests.get(url)
tabla = data.json()

#print( json.dumps(data.json(), indent=4, separators=(",",":")))
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

with open("bitso.txt") as f:
        content = f.readlines()

h_string = content[0]
l_string = content[1]

dicc_l = dict(s.split(':', 1) for s in l_string.split())  

lowest = dicc_l["lowest"]
lowest_dia = dicc_l["dia"]
lowest_hora = dicc_l["hora"]

#lowest_time = tabla["payload"]["created_at"]

dicc_h = dict(s.split(':', 1) for s in h_string.split())

highest = dicc_h["highest"]
highest_dia = dicc_h["dia"]
highest_hora = dicc_h["hora"]

#highest_time = tabla["payload"]["created_at"]


db = influxdb.InfluxDBClient("172.16.1.100", 8086, "paco", "paco", "example")
data = [{"measurement":"Crypto-XRP","fields":{"Alto":float(high),"Bajo":float(low),"Actual":float(last)}}]
db.write_points(data)

file = open('bitso.txt', 'w')

if float(high) > float(highest):
    highest = high
    highest_time_time = time
    file.write("highest:"+highest+"\t"+"dia:"+dia+"\t"+"hora:"+hora+"\n")
else:
    file.write("highest:"+highest+"\t"+"dia:"+highest_dia+"\t"+"hora:"+highest_hora+"\n") 
    print ("Sin cambio")


if float(low) < float(lowest):
    lowest = low
    lowest_time = time
    file.write("lowest:"+lowest+"\t"+"dia:"+dia+"\t"+"hora:"+hora+"\n")
else:
    file.write("lowest:"+lowest+"\t"+"dia:"+lowest_dia+"\t"+"hora:"+lowest_hora+"\n")
    print ("Sin cambio")

print ("\n","\t",)
print ("Alto :",highest,"\tBajo :",lowest, "@" ,dia, hora) 
print ("\n\t",)
print ("\n\t","Ultimo Valor :", last)

#file = open('bitso.txt', 'w')
#file.write("highest:"+highest+"\t"+"dia:"+dia+"\t"+"hora:"+hora+"\n")
#file.write("lowest:"+lowest+"\t"+"dia:"+dia+"\t"+"hora:"+hora+"\n")
file.close()
