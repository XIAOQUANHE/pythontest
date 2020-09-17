# 1. 写一个函数get_digits(n)，将参数n分解出每个位的数字并按顺序存放到列表中。举例：get_digits(12345) ==> [1, 2, 3, 4, 5]
# insert()  方法语法：L.insert(index,obj)
result = []
def get_digits(n):
    if n > 0:
        result.insert(0,n%10)   # Python 列表 insert() 方法将指定对象插入到列表中的指定位置。 求个位数
        # print(n%10)           # 5,4,3,2,1
        get_digits(n//10)

get_digits(12345)
print(result)