import os
import configparser
import getpathInfo

path = getpathInfo.get_path()  #调用实例化方法
config_path = os.path.join(path,"config.ini")
config = configparser.ConfigParser() #调用外部的读取配置文件方法
config.read(config_path,encoding="utf-8")

class ReadConfig():

    def get_http(self,name):
        value = config.get('HTTP',name)
        return value

    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value

    def get_mysql(self, name):  #
        value = config.get('DATABASE', name)
        return value


if __name__ == '__main__':
    print("HTTP中baseurl值为：",ReadConfig().get_http('baseurl'))
    print("EMAIL中开关on_off值为：",ReadConfig().get_email('on_off'))


