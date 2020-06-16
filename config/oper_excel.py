import xlwt
import xlrd
import requests
import json
import re
# from Interface_Automation.config.logg import logg
class Test1():

    num = 0  # 类属性

    def __init__(self):
        # 初始化方法，获取cookies
        self.url = "https://api.quwank.com/login/submit"

        self.data = {
            "phone": 15617816225,
            "password": 123456
        }

        self.response = requests.post(self.url,data = self.data)

        # print(self.response.cookies.get_dict()["SESSION"])

        self.cookies = self.response.cookies.get_dict()
        # print(self.cookies,"init__cookies")
        # return self.response.cookies.get_dict()["SESSION"]

    def get_col(self,i):
        # 获取excel文件中每行数据
        row = table.row_values(i)
        return row

    def test(self,j):
            Test1.num += 1  #进行一次函数num+1，确定异常出现行数
            # 当前行的数据
            getdata = self.get_col(j)
            # 判断请求类型
            self.url = getdata[0]
            data = json.loads(getdata[2])
            # 是否需要鉴权
            number = int(getdata[5])
            # print(number)

            # /*判断请求类型*/
            if getdata[1] == "POST":
                if number == 1:
                    response = requests.post(self.url,data = data,cookies = self.cookies)#headers = json.loads(getdata[3]))
                else:

                    response = requests.post(self.url,data = data,)#headers = json.loads(getdata[3]))
            #
            else:
                if number == 1:
                    response = requests.get(self.url, params=data, headers=json.loads(getdata[3]),cookies = self.cookies)
                elif number == 0:
                    response = requests.get(self.url, params=data, headers=json.loads(getdata[3]))

            self.jsondict = json.loads(response.text)  #json字符串转为字典，
            # print(response.cookies)


            print(self.checkResponse())


    def checkResponse(self):
        msg = self.jsondict["msg"]  # 取出key=msg的值

        if self.jsondict["code"] != "0000":
            result = ("第%s个%s接口错误，返回值:%s" % (Test1.num, self.url, msg))

            with open("D:\myCode\Interface_Automation\config\log.txt", "a+") as f:
                f.write(result + "\n\t")

            return result
        else:
            result = "pass" + "," + self.jsondict["msg"] + "," + str(self.jsondict["data"])
            # status = "pass"
            # status + "," + result
            with open("D:\myCode\Interface_Automation\config\log.txt", "a+", encoding="GBK") as f:
                f.write(result + "\n\t")
            return result



if __name__ == '__main__':
    # data = xlrd.open_workbook("data.xlsx")
    # 通过excel里面的表名获取工作表
    table = xlrd.open_workbook("D:\myCode\Interface_Automation\config\data.xlsx").sheet_by_name("Sheet1")
    # 通过索引获取工作表
    # table1 = data.sheet_by_index(0)
    # table2 = data.sheets()[0]
    #
    # # 通过表名的索引获取工作表
    # table3 = data.sheet_names()[0]
    # # 获取表第一行的数据
    # # # row = table.row_values(0)
    # row2 = table.row_values(1)

    ncol = table.ncols
    # print(ncol, "ncol"
    #       )  # 获取列数
    nrow = table.nrows  # 获取行数
    # print(nrow,"nrow")

    # 开始执行时，先删除以前log数据
    with open("D:\myCode\Interface_Automation\config\log.txt","r+") as f:
        f.truncate(0)

    print("验证构建是否成功")
    print("验证构建是否成功2")
    print("验证构建是否成功3")
    print("验证构建是否成功4")





    for i in range(nrow-1):
        print(i+1)
        test = Test1()
        print(test.test(i + 1))



