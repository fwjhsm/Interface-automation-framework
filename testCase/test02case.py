import unittest

import paramunittest

from readExcel import readExcel
from getpathInfo import get_path
import readExcel

login_xls = readExcel.readExcel().get_xls("userCase.xlsx","login")

print(login_xls)
# @paramunittest.parametrized(*login_xls)
class testLogin(unittest.TestCase):

    def setUp(self,*login_xls):

        self.data = login_xls[0][1]
        self.path = get_path()



    def test01case(self):

        return self.data


    def tearDown(self):
        pass



# print(Login().test01case())