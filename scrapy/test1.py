#!/usr/bin/python
# -*- coding: utf-8 -*-

# Engine 引擎 核心 处理真个系统数据流 触发事务   item 定义爬取结果的数据结构，爬取的数据会赋值成item对象
# Scheduler 调度器 接受引擎发出的请求并加入队列中，当引擎再次请求时再提供给引擎  Downloader 下载器 将网页内容返回给spider
# Spider 定义爬取的规则 和网页的解析规则 ，主要负责解析响应提取结果  item Pipeline 项目管道 负责spider 的清洗 验证 存储数据
# Downloader Middlewares 下载中间件 位于引擎和下载器之间，主要处理引擎和下载器之间的响应
# spider Middlewares spider中间件 位于引擎和spider之间 处理spider的响应和输出结果

# 数据流  1.engine打开一个网站，找到该网站的spider 请求第一个url
#        2.engine从Spider中获取第一个爬取的url，通过Scheduler和Requests形式调度
#        3.engine想Scheduler请求下一个url
#        4.Scheduler返回一个url，engine通过Downloader Middlewares 转给Downloader
#        5.Downloader将response通过Downloader Middlewares 转给engine
#        6.engine通过spider middlewares 发给spider处理
#        7.spider处理response,并返回item和requests 给 engine
#        8.engine将spider返回的item gei itemPipeline

