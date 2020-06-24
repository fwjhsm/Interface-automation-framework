import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
# import pythoncom
import readExcel


url = geturlParams.geturlParams().get_Url()  #调用我们的geturlParams获取我们拼接的URL

print(url, "url")
login_xls = readExcel.readExcel().get_xls("userCase.xlsx", 'login')  #调用excel中的用例
print(login_xls,"login_xls")
print(*login_xls,"*login_xls")

@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):
        # setParameters
        """
        :param case_name:
        :param path:
        :param query:
        :param method:
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """

        :return:
        """
        print(self.case_name+"测试开始前准备")


    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输入log完结\n\n")

    def checkResult(self):
        """

        :return:
        """

        url1 = "http://127.0.0.1:8888/login?"
        new_url = url1 + self.query

        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))# 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        print(data1,"data1 1")

        # info = RunMain().run_main(self.method,url,self.query)
        info = RunMain().run_main(login_xls[0][3],url,login_xls[0][2])

        print(info,"info")
        ss = json.loads(info) #json 转字典
        print(ss,"ss")
        if self.case_name == "login":
            self.assertEquals(ss["code"], 200)

        if self.case_name == "login_error":
            self.assertEquals(ss["code"], -1)

        if self.case_name == "login_null":
            self.assertEquals(ss["code"], 10001)




# testUserLogin().test01case()