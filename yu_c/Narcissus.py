'''用函数求100-1000的所有水仙花数'''
def Narcissus():
    for each in range(100,1000):
        temp = each
        sum = 0
        while temp:
            sum = sum +(temp%10)**3
            temp = temp // 10   # 用地板除，返回int型

        if sum == each:
            print(each , end='\t')

print("所有的水仙花数分别是：", end='')
Narcissus()