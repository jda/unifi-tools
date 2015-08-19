#!/usr/bin/env python
from pymongo import MongoClient
import json
import sys

# print message and die
def msgDie(msg):
	print msg
	sys.exit(2)

if len(sys.argv) != 2:
	msgDie("usage: unifi-countap.py config.json")

# load config
cfgFile = sys.argv[1]

with open(cfgFile) as data_file:    
    cfg = json.load(data_file)

# get database
dbCfg = cfg['database']
client = MongoClient(dbCfg['host'], dbCfg['port'])
db = client[dbCfg['db']]

devcounts = {}

devices = db['device']
for device in devices.find():
	model = device["model"]
	
	try:
		count = devcounts[model]
	except KeyError:
		count = 0
	
	count += 1
	
	devcounts[model] = count

total = 0
for k, v in devcounts.iteritems():
	print "%s: %s" % (k, v)
	total += v
print "Total: %s" % (total)
