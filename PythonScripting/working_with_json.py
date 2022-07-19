#!/usr/bin/python3

import json

req_file='sample.json'

fo=open(req_file,'r')

#print(fo.read())
print(json.load(fo))

fo.close()
