# 使用递归编写一个 power() 函数模拟内建函数 pow()，即 power(x, y) 为计算并返回 x 的 y 次幂的值。

def gcd(x,y):
    if y :
        return gcd(y,x%y)
    else:
        return x

print(gcd(4,4))