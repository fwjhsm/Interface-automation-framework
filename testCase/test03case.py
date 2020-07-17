#user/test02case
import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
from common.sessionDB import Session
# import pythoncom
import readExcel
# pythoncom.CoInitialize()

url = geturlParams.geturlParams().get_Url_https_pay()# 调用我们的geturlParams获取我们拼接的URL

login_xls = readExcel.readExcel().get_xls('userCase.xlsx', 'sc_pay')
                                                           #新增接口需修改


@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):

    def setParameters(self, case_name, path, query, method,remark,auc):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)
        self.remark = str(remark)
        self.auc = str(auc)

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
        print("测试结束，输出log完结\n\n")

    def checkResult(self):# 断言
        """
        check test result
        :return:
        """
        url1 = "https://frontsm.quwank.com/api/order/placeOrder?"  #新增接口需修改
        new_url = url1 + self.query
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))# 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}


        print(data1,"data1---test03")

        print(self.auc)
        print(type(self.auc))

        if self.auc == "1.0":

            # 若auc =1 ，则需要鉴权
            info = Session().run_main(self.method,url,data1)
            response = info.json()

        elif self.auc == "0.0":
            info = RunMain().run_main(self.method, url, data1)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
            print(info, "info")
            print(type(info), "info的类型")
            response = json.loads(info)  # 将响应转换为字典格式
        else:
            response = None
            return "auc值错误"

        if self.case_name == 'pay':# 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(response['msg'], self.remark)
            print(response['code'])

            print(info)

        if self.case_name == 'pay_null':# 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(response['msg'], self.remark)
            print(response['msg'])

        #
        # if self.case_name == 'login_error':# 同上
        #     self.assertEqual(response['msg'], self.remark)
        #     print(response['code'])
        #
        # if self.case_name == 'login_error2':# 同上
        #     self.assertEqual(response['msg'], self.remark)
        #     print(response['code'])
        #
        # if self.case_name == "login_null":
        #     self.assertEqual(response['msg'],self.remark)



    # return self.assertEquals(ss["code"],)


# testUserLogin().test01case()