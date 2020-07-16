import readConfig

readconfig = readConfig.ReadConfig()

class geturlParams():  #定义一个类，将从配置文件中读取的进行拼接
    def get_Url_https(self):
        new_url = readconfig.get_https("scheme") + "://" + readconfig.get_https('baseurl')
        # new_url = readconfig.get_http('baseurl') + ":"+ readconfig.get_http("port")+"/login"+"?"
        return new_url

    def get_Url_http(self):
        # new_url = readconfig.get_https("scheme") + "://" + readconfig.get_https('baseurl')
        new_url = readconfig.get_http("scheme") + "://" + readconfig.get_http('baseurl') + ":"+ readconfig.get_http("port")+"/login"+"?"
        return new_url

if __name__ == '__main__':
    print(geturlParams().get_Url_https())
    print(geturlParams().get_Url_http())
