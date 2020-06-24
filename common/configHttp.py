import requests
import json
from geturlParams import geturlParams

class RunMain():

    def send_post(self,url,data):
        #参数必须按照URL、data的顺序传入
        result = requests.post(url = url,data=data).json()
        res = json.dumps(result,ensure_ascii=False)
        return res
    def send_get(self,url,data):
        result = requests.get(url = url,params=data).json()
        res = json.dumps(result,ensure_ascii=False)
        return res
    def run_main(self,method,url=None,data=None):
        result = None
        if method == "post":
            result = self.send_post(url,data)

        elif method == "get":
            result = self.send_get(url,data)

        else:
            print("method值错误")
            return {"message": "method值错误"}

        return result

if __name__ == '__main__':
    result = RunMain().run_main("get",'http://127.0.0.1:8888/login',{'name': 'xiaoming','pwd':'123456'})


    # result  = RunMain().run_main()
    print(result)