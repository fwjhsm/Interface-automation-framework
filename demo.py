import requests
import unittest

# import HTMLTestRunner

s = requests.Session()

class test():

    url = " http://127.0.0.1:8888/login"
    url1 = "https://frontsm.quwank.com/api/login"
    data = {
        "phone": "15617816228",
        "password": 123456,
        "type": 2

    }
    data1 = {
        "phone": "15617816228",
        # "password": 123456,
        "type": 1

    }

    def get_code(self):

        res = requests.post(self.url,data = self.data1)

        res1 = s.post(url=self.url1,data=self.data,)

        print(res.cookies["SESSION"])
        print(res.cookies)
        print(res1.text)
        print(res.text)
        print(requests.sessions.get_environ_proxies,"session取值" )

        return s


    def s(self):
        t1.get_code()
        url = "https://frontsm.quwank.com/api/order/placeOrder"
        data = {
            "discountAmount":0,
            "goodsTotalAmount":2100,
            "payableAmount":2100,
            "totalAmount":2100,
            "check.totalAmount":2100,
            "check.noDiscountAmount":0,
            "phone":15617816228,
            "storeId":117,
            "type":5




        }
        res = s.post(url,data)
        print(res.text)
        print(res.json())
        print(res.raw)
        print(res.request)
        pass


# get_code()

def login_post():
    url =  "http://127.0.0.1:8888/login"
    data = {
        "name":"xiaoming",
        "pwd":123456
    }

    res = requests.post(url = url,data=data)
    print(res)
    print(res.text)

# t1 = test()
# t1.get_code()
# t1.s()

login_post()