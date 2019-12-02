import xlwt
import xlrd
import requests
import json
# import urlbm
data = xlrd.open_workbook("data.xlsx")

# 通过excel里面的表名获取工作表
table = data.sheet_by_name("Sheet1")

# 通过索引获取工作表
table1 = data.sheet_by_index(0)
table2 = data.sheets()[0]

# 通过表名的索引获取工作表
table3 = data.sheet_names()[0]

# 获取表第一行的数据
# row = table.row_values(0)
row2 = table.row_values(1)

# ncol = table.ncols
# print(ncol,"ncol"
#       )    #获取列数
nrow = table.nrows   #获取行数
# print(nrow,"nrow")

class Test1():

    def get_col(self,i):
        row = table.row_values(i)
        return row


    def test(self,j):

        if self.get_col(j)[1] == "POST":
            url = self.get_col(j)[0]
            data = self.get_col(j)[2].encode("UTF8")
            response = requests.post(url,data=self.get_col(j)[2],headers = json.loads(self.get_col(j)[3]))
            print(response.text)
            print(response.url)
            return response.text



        elif self.get_col(j)[1] == "GET":
            url = self.get_col(j)[0].decode("utf-8")
            data = self.get_col(j)[2]
            print(data)

            response = requests.get(url,params = data,headers = json.loads(self.get_col(j)[3]))
            print(response.text)
            print(response.url)

            return response.text



if __name__ == '__main__':
    for i in range(nrow-1):
        print(i)
        test = Test1()
        test.test(i + 1)
        # if i == nrow - 1:
        #     break

