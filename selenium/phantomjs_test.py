from selenium import webdriver
from scrapy import signals
from selenium import  webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger

browser = webdriver.Chrome()
browser.get('https://s.taobao.com/search?q=iPad')
print(browser.page_source)
