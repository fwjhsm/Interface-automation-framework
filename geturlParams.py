import readConfig

readconfig = readConfig.ReadConfig()

class geturlParams():  #定义一个类，将从配置文件中读取的进行拼接
    def get_Url(self):
        new_url = readconfig.get_http("scheme") + "//" + readconfig.get_http('baseurl')+':8888' + '\login' + '?'
        return new_url


if __name__ == '__main__':
    print(geturlParams().get_Url())