import json

import requests


session = requests.Session()


class Session():
    url = "https://frontsm.quwank.com/api/login"
    data = {
        "phone": "15617816228",
        "password": 123456,
        "type": 2
    }
    # def get_data(self,url,data):
    #     self.url = url
    #     self.data = data

    def get_cookie(self):
        session.post(self.url,self.data)

        return session

    def session_post(self,url,data):
        self.get_cookie()
        result = session.post(url=url,data=data)
        return result
    def session_get(self,url,data):
        self.get_cookie()
        result = session.get(url=url,data=data)
        return result

    def run_main(self,method,url=None,data=None):
        result = None
        if method == "post":
            result = self.session_post(url,data)

        elif method == "get":
            result = self.session_get(url,data)

        else:
            print("method值错误")
            return {"message": "method值错误"}

        return result


if __name__ == '__main__':
    # Session().get_data()
    print(Session().get_cookie())
    print(Session().session_post())