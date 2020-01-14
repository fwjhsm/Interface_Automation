import xlwt
import xlrd
import requests
import json



class Test1():


    num = 0  # 类属性

    def get_col(self,i):
        # 获取excel文件中每行数据
        row = table.row_values(i)
        return row


    def test(self,j):
            Test1.num += 1  #进行一次函数num+1，确定异常出现行数

            # 判断请求类型
            url = self.get_col(j)[0]
            data = self.get_col(j)[2]

            # /*判断请求类型*/
            if self.get_col(j)[1] == "POST":
                response = requests.post(url,data = data,headers = json.loads(self.get_col(j)[3]))
            elif self.get_col(j)[1] == "GET":
                response = requests.get(url, params=data, headers=json.loads(self.get_col(j)[3]))

            jsondict = json.loads(response.text)  #json字符串转为字典，

            msg = jsondict["msg"]   #取出key=msg的值

            if jsondict["result"] != "success":
                result = ("第%s行%s接口错误，返回值:%s" % (Test1.num + 1, url, msg))
                return result
            else:
                result = jsondict["result"]
                return result


    def checkReponse(self):
        return


if __name__ == '__main__':
    data = xlrd.open_workbook("data.xlsx")
    # 通过excel里面的表名获取工作表
    table = data.sheet_by_name("Sheet1")
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

    for i in range(nrow-1):
        print(i+1)
        test = Test1()
        print(test.test(i + 1))


