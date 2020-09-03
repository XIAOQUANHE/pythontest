# nums = '11111111111'
# print(len(nums))

# 视频中我们说sum()这个BIF有个缺陷，就是如果参数里有字符串类型的话就会报错，写出一个新的实现过程，自动“无视”参数里的字符串并返回正确的计算结果

def sum(x):
    result = 0

    for each in x:
        if (type(each) == int) or (type(each) == float):
            result += each
        else:
            continue
    return result

print(sum([1,2.1,3.1,'a','1',True]))