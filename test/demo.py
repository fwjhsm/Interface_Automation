import json
import requests
num = 0.01
#
# sum = 30
#
# sum1 = 0
# i= 0
# S = 1
# while S:
#
#     num += 0.01
#     sum1 += num
#     if sum1 >= sum:
#         S = 0
#         break
#     i += 1
#
#     print(i,"次数")
#     print( "总钱数%.2f"%sum1)
#     print("最后一次的钱:%.2f"%num)
#     print("\r")


def post():
    url = "https://api.quwank.com/login/submit"
    url1 = "https://api.quwank.com/goods/spuDetail"
    data = {
        "phone":15617816228,
        "password":123456
    }

    print(type(data))
    data1 = {

        "spuId":65,
        "skuId":193,
        "type":1
    }

    response = requests.post(url=url1,data =data1)



    print(response.status_code)
    print(response.text)
    print(response.content)
    print(response.headers)


print(post())