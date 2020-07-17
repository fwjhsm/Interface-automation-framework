import os
import getpathInfo  #定义的内部类，该类返回项目的绝对路径
from xlrd import open_workbook


#该项目所在的绝对路径
path = getpathInfo.get_path()
print(path)

class readExcel():
    def get_xls(self,xls_name,sheet_name):
        cls = []
        # 获取用例文件路径
        xlsPath = os.path.join(path,"testFile\case",xls_name)
        file = open_workbook(xlsPath)
        # print(xlsPath)

        sheet = file.sheet_by_name(sheet_name)

        nrows = sheet.nrows
        # print(nrows)
        for i in range(nrows):
            if sheet.row_values(i)[0] != 'case_name':
                cls.append(sheet.row_values(i))

        return cls

if __name__ == '__main__':
    print(readExcel().get_xls('userCase.xlsx','sc_login'))
    print(readExcel().get_xls('userCase.xlsx','sc_login')[0][1])
    print(readExcel().get_xls('userCase.xlsx','sc_login')[0][2])

    print(readExcel().get_xls('userCase.xlsx','sc_pay')[0][2])
