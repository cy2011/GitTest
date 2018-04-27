# coding:utf-8
import unittest
import os
import projectone.HTMLTestRunner_report
import time

# python2.7要是报编码问题，就加这三行，python3不用加
'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')
'''
cur_path = os.path.dirname(os.path.realpath(__file__))#获取的__file__所在脚本的路径
case_path = os.path.join(cur_path, "testcase")        # 测试用例的路径
report_path = os.path.join(cur_path, "report")  # 报告存放路径
print(cur_path)
if __name__ == "__main__":
    # testcase目录查找测试用例文件（test*.py）
    discover = unittest.defaultTestLoader.discover(case_path,"test*.py")
    #print(discover)
    #输出当前时间
    now = time.strftime('%Y-%m-%d-%H-%S')
    #测试报告名字
    filename = report_path + '/testResult_' + now + '.html'
    fp = open(filename, 'wb')
    run = projectone.HTMLTestRunner_report.HTMLTestRunner(title="测试报告",
                                            description="测试用例参考",
                                            stream=fp)

    run.run(discover)
    fp.close()