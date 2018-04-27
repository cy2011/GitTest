# coding:utf-8
from selenium import webdriver
import unittest
from projectone.common.base import BaseCommon
url = "https://www.baidu.com"
class Test1(unittest.TestCase):
    '''
    classmethod 修饰符对应的函数不需要实例化，
    不需要 self 参数，
    但第一个参数需要是表示自身类的 cls 参数，
    可以来调用类的属性，类的方法，实例化对象等。
    '''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        u"""定位失败截图案例"""
        BaseCommon(self.driver).openUrl(url)
        BaseCommon(self.driver).untilTime("ID","xxx").send_keys(u'百度一下')
        BaseCommon(self.driver).untilTime("ID", "su").click()
        self.assertTrue(True)

    def test_02(self):
        u'''失败用例'''
        BaseCommon(self.driver).openUrl(url)
        t = self.driver.title
        self.assertIn(u"失败用例",t)

    def test_03(self):
        u'''通过用例'''
        BaseCommon(self.driver).openUrl(url)
        self.assertIn(u"百度",self.driver.title)


if __name__ == "__main__":
    unittest.main()
