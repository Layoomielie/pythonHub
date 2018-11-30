#!/usr/bin/python
# -*- coding: utf-8 -*-

url='http://my.cnki.net/elibregister/commonRegister.aspx'

import tesserocr
from PIL import Image

image=Image.open('code.jpg')
result=tesserocr.image_to_text(image)
print(result)