

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from twisted.conch.telnet import EC

email='test@test.com'
PassWord='123456'
class CrackGeetest():
    def __init__(self):
        self.url='https://account.geetest.com/login'
        self.brower=webdriver.chrome()
        self.wait=WebDriverWait(self.brower,20)
        self.email=email
        self.password=PassWord

def get_geetest_button(self):
    button=self.wait.until()