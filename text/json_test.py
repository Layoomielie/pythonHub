#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

str = """
[{
"name":"Bob",
"gender":"male",
"birthday":"1992-10-18"
},{
"name":"Selina",
"gender":"female",
"birthday":"1995-10-18"
}]
"""
data = json.loads(str)
# print(data)
# print(data[0].get('name'))

with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(str, indent=2, ensure_ascii=False))
