#!/usr/bin/python
# -*- coding: utf-8 -*-
import  re

content='Hello 123 4567a World_This is a Regex Demo'

print(len(content))

#result=re.match('^Hello\s\d{3}\s(\d+)\s\S{7,20}',content)
result=re.match('^Hello.*?(\d+\s\w*).*?Demo$',content)
print(result)
print(result.span())
print(result.group(1))