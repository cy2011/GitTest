# -*- coding: utf-8 -*-
import sys
sys.path.append("/Users/yangcy/Desktop/python/test/seleniumMZ")
from projectone.common.base import BaseCommon
from projectone.common.util import Util
from projectone.public.login import Mylogin
from selenium import webdriver
import unittest
import os
import time

class Testlogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver     = webdriver.Firefox()
        cls.basecommon = BaseCommon(cls.driver)
        cls.mylogin    = Mylogin(cls.driver)
        cls.data       = Util().operateYaml("/Users/yangcy/Desktop/python/test/seleniumMZ/data/pageData/pageData.yaml")
        # 取到yaml里面的所有数据
        cls.basecommon.openUrl(cls.data['login']['url'])
        time.sleep(3)

    '''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.basecommon = BaseCommon(self.driver)
        self.mylogin    = Mylogin(self.driver)
        self.data       = Util().operateYaml("/Users/yangcy/Desktop/python/test/seleniumMZ/data/pageData/pageData.yaml")
        #取到yaml里面的所有数据
        self.driver.get(self.data['login']['url'])
        time.sleep(5)
    '''
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def testMaizi01_01(self):
        u"""账号密码登录成功，并成功退出"""
        time.sleep(2)
        self.mylogin.login()
        self.mylogin.out()
        #self.assertTrue(True)
        #print "sucess"

if __name__ == "__main__":
    unittest.main()