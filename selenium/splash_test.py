#!/usr/bin/python
# -*- coding: utf-8 -*-

# js_enabled 控制JS代码是否执行   resource_timeout 控制加载超时时间  images_enabled 设置图片是否加载

# plugins_enabled 控制浏览器插件是否开启   scroll_position  控制页面上下滚动  .scroll_position={y=400}

# splash:go 请求某个链接

# splash:go{url,baseurl=nil , headers=nil ,http_method="get",body=nil,formdata=nil}

# url 请求参数  baseurl 资源加载相对路径 可以为空  body默认为空 发post请求的表单数据

# jsfunc()可以调用JS中的方法  evaljs 执行js代码.返回最后一条结果 runjs  执行js代码  偏向于执行动作或声明方法

# aotoload() 此方法设置每个页面访问时自动加载对象  call_later 设置定时任务和延迟时间来实现任务延迟执行

# http_get() 此方法模拟发送Http的GET请求， http_post post请求

# set_content 设置页面内容  html 获取网页源代码  png 获取网页截图 jpeg  har 获取网页加载过程描述  url获取当前正在访问页面的url

# get_cookies()  add_cookies() clear_cookies() get_viewport_size() 获取当前浏览器页面大小 set_viewport_size set_viewport_full

# set_user_agent 设置User-Agent  set_custom_headers 设置请求头  select  会选中符合条件的第一个节点 select_all会选择符合条件的所有节点

# mouse_click 模拟鼠标点击

# splash api的调用  加载渲染后的页面  后面可以 添加参数 wait等待秒数  还支持代理 图片加载 headers等设置

import requests
# url='http://localhost:8050/render.html?url=https://www.baidu.com'
# response=requests.get(url)
# print(response.text)

# render.png  此接口可以获取网络截图 通过width  height来控制宽高  获取页面图片

# url='http://localhost:8050/render.png?url=https://www.jd.com&wait=5&width=1000&height=700'
# response=requests.get(url)
# with open('tabao.png','wb') as f:
#     f.write(response.content)

# render.jpeg render.har  render.json 放回的是json格式

# execute是非常强大的接口 此接口可以和lua脚本对接

from urllib.parse import quote
lua= '''
function main(splash)
    return 'hello'
end
'''

url='http://localhost:8050/execute?lua_source='+quote(lua)
response=requests.get(url)
print(response.text)

# 此处用三引号将lua脚本包括起来，用parse中的quote方法将脚本url转码，构造了 splash请求url 将其作为lua_source的参数传递

# splash的负载均衡 需要拥有多个splash服务

