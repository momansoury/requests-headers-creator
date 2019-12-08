#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
data = str(raw_input("\n[#]Header>>>\n\n")).decode('base64')

data2 = data.split("\n")
result = {}
for x in data2:
	value, key = x.strip("\r").replace(" ", '').split(":", 1)
	result[value] = key
with open('headers.txt', 'w') as hd:
	hd.write(str(result))
hd.close()
os.popen("headers.txt")
