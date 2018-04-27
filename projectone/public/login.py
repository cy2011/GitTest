#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import unittest,time
from projectone.common.util import Util
from projectone.common.base import BaseCommon
from selenium import webdriver
import os
logindatapath = "/Users/yangcy/Desktop/python3/projectone/data/inputData/loginData.yaml"
pagedatapath  = "/Users/yangcy/Desktop/python3/projectone/data/pageData/pageData.yaml"
class Mylogin:
    def __init__(self,driver):
        self.driver = driver
        #初始化登录的数据
        self.data     = Util().operateYaml(logindatapath)
        #print self.data['login']['login_data_01']['username']
        self.username = self.data['login']['login_data_01']['username']
        #print self.username
        self.password = self.data['login']['login_data_01']['pwd']
        self.pagedata = Util().operateYaml(pagedatapath)
    '''
    
    def login(self):
        self.driver.find_element_by_id(self.pagedata['login']['name']).send_keys(self.username)
        self.driver.find_element_by_id(self.pagedata['login']['password']).send_keys(self.password)
        self.driver.find_element_by_id(self.pagedata['login']['loginButton']).click()
        time.sleep(3)
    '''
    #下面跟上面注释掉的功能一样，下面调用函数
    def login(self):
        BaseCommon(self.driver).untilTime("ID",self.pagedata['login']['name']).send_keys(self.username)
        BaseCommon(self.driver).untilTime("ID",self.pagedata['login']['password']).send_keys(self.password)
        BaseCommon(self.driver).untilTime("ID",self.pagedata['login']['loginButton']).click()
    def out(self):
        BaseCommon(self.driver).untilTime('ID',self.pagedata['out']['outid']).click()
