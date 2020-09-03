''' 编写一个将十进制转换为二进制的函数，要求采用“除2取余”（补脑链接）的方式，结果与调用 bin() 一样返回字符串形式。
	格式：bin(111)——>0b1101111'''
def Dec2Bin(dec):
    temp = []
    result = ''

    while dec:
        quo = dec % 2
        dec = dec // 2 # 返回int型，如果dec/2 会有小数点
        temp.append(quo)

    while temp:     # 这是列表，为空结束循环
        result += str(temp.pop()) # 从尾部删除数据，并打印出来

    return result

print(Dec2Bin(22))
print(bin(22))