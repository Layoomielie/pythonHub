#!/usr/bin/python
# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input=browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait=WebDriverWait(browser,10)
#     wait.until(EC.presence_of_all_elements_located((By.ID,'content_left')))
#     print(browser.current_url)
#     print(browser.page_source)
#
# finally:
#     browser.close()
#
# # clear会清空文字  click点击按钮

from selenium.webdriver import ActionChains
url="https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
browser.get(url)
browser.switch_to_frame('iframeResult')
source=browser.find_element_by_css_selector('#draggable')
target=browser.find_element_by_css_selector('#droppable')
actions=ActionChains(browser)
actions.drag_and_drop(source,target)
actions.perform()

# get_attribute 可以获得节点的属性  .text 可以获得元素的文本
# 隐式延迟等待
browser.implicitly_wait(10)
# 显式延迟等待 设置时间等待节点加载
wait=WebDriverWait(browser,10)

# forward 前进  back 回退


