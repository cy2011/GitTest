#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BaseCommon:
    def __init__(self,driver):
        self.driver = driver
    def openUrl(self,url):
        self.driver.get(url)
    def untilTime(self,attrib,attrCont):
        if attrib == 'ID':
            elem = WebDriverWait(self.driver,5,0.5).until(
                EC.presence_of_element_located((By.ID,attrCont))
            )
        return elem
url ="http:www.baidu.com"
driver = webdriver.Firefox()
x =BaseCommon(driver)
x.openUrl(url)
x.untilTime('ID','kw').send_keys("ddd")

driver.quit()