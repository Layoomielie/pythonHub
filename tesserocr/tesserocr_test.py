#!/usr/bin/python
# -*- coding: utf-8 -*-

url='http://my.cnki.net/elibregister/commonRegister.aspx'

import tesserocr
from PIL import Image

# image=Image.open('code.jpg')
# result=tesserocr.image_to_text(image)
# print(result)

# 将图片转化为灰色图像 convect 方法参数传入L
image=Image.open('code2.jpg')
image=image.convert('L')        #转化为灰色图像
threshold=127
table=[]
for i in range(256):            # 确定阈值
    if i<threshold:
        table.append(0)
    else:
        table.append(1)

image=image.point(table,'1')
result=tesserocr.image_to_text(image)
print(result)

# image=Image.open('image.png')
# print(tesserocr.image_to_text(image))
