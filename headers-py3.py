#!/usr/bin/python3
# -*- coding: utf-8 -*-

import base64 as bs

data = bs.standard_b64decode(input("\n[#]Header>>>\n\n"))
data2 = data.decode().split("\n")
result = {}
for x in data2:
	value, key = x.strip("\r").strip().split(":", 1)
	result[value] = key
with open('headers.txt', 'w') as hd:
	hd.write(str(result))
hd.close()
