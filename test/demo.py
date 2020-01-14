import json

num = 0.01

sum = 30

sum1 = 0
i= 0
S = 1
while S:

    num += 0.01
    sum1 += num
    if sum1 >= sum:
        S = 0
        break
    i += 1

    print(i,"次数")
    print( "总钱数%.2f"%sum1)
    print("最后一次的钱:%.2f"%num)
    print("\r")