import json
import os
# import urllib
import urllib.parse

from common.configHttp import RunMain
from getpathInfo import get_path
from getpathInfo import get_path
import readConfig

path = get_path()
report_path = os.path.join(path, 'result')
on_off = readConfig.ReadConfig().get_email('on_off')


resultPath = os.path.join(report_path, "report.html")  # result/report.html
caseListFile = os.path.join(path, "caselist.txt")  # 配置执行哪些测试文件的配置文件路径
print(caseListFile, "caseListFile")
caseFile = os.path.join(path, "testCase")  # 真正的测试断言文件路径
caseList = []

print(os.path)

print(caseFile,"caseFile")
print(caseList,"caseList")


def checkResult():  # 断言
    """
    check test result
    :return:
    """
    method  = "post"

    query = """phone=15617816228&password=123456"""
    # query = {
    #     "phone":"15617816228",
    #     "password":"123456"
    # }
    url = "https://api.quwank.com/login/submit?"
    url1 = "https://api.quwank.com/login/submit?"
    new_url = url1 + query
    data1 = dict(urllib.parse.parse_qsl(
        urllib.parse.urlsplit(new_url).query))  # 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}

    print(data1)
    info = RunMain().run_main(method, url, data1)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
    ss = json.loads(info)  # 将响应转换为字典格式

    print(ss)


checkResult()