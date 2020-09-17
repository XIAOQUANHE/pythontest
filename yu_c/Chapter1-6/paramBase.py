'''编写一个符合以下要求的函数：
    a) 计算打印所有参数的和，乘以基数 (base=3)的结果
    b） 如果参数中最后一个参数为(base=5)，则设定基数为5，基数不参与求和计算。'''

def mFun(*param, base = 3):
    result = 0
    for each in param:
        result += each
    result *= base

    print('结果是：', result)

mFun(1,2,3,4,5,base=5)