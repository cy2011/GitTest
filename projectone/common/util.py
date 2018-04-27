# -*- coding: utf-8 -*-
'''
comment目录下，建立 util.py  和base.py

'''
import yaml
class Util(object):
    def __init__(self):
        pass
    def operateYaml(self,filename):
        file = open(filename,"r")
        data = yaml.load(file)
        file.close()
        return data
