#!/usr/bin/env python
from pymongo import MongoClient
import json
import sys

# print message and die
def msgDie(msg):
	print msg
	sys.exit(2)

if len(sys.argv) != 4:
	msgDie("usage: unifi-minder.py config.json site-name minSNR")

# load config
cfgFile = sys.argv[1]
siteName = sys.argv[2]
minSNR = sys.argv[3]

with open(cfgFile) as data_file:    
    cfg = json.load(data_file)

print cfg
# get database
dbCfg = cfg['database']
client = MongoClient(dbCfg['host'], dbCfg['port'])
db = client[dbCfg['db']]

sites = db['site']
site = sites.find_one({"name": siteName})

sid = str(site["_id"])

devices = db['device']
for device in devices.find({"site_id": sid}):
	mac = device["mac"]
	mac = mac.replace(":", "")
	for radio in device['radio_table']:
		radtype = radio['radio']

		print "config.minrssi.%s.%s=%s" % (mac, radtype, minSNR)

 
