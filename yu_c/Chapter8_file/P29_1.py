# 1. 编写一个程序，比较用户输入的两个文件，如果不同，显示出所有不同处的行号与第一个不同字符的位置

def file_compare(file_one,file_two): # 函数接收形参
    f1 = open(r"../test_data/%s"%file_one)  # 打开用户输入的文件名
    f2 = open(r"../test_data/%s"%file_two)  # 打开用户输入的另一个文件名
    count = 0 # 统计行数
    differ = [] # 统计不一样的数量

    for line1 in f1:    # 取一行数据
        line2 = f2.readline() # 取一行数据
        count += 1  # 统计行数+1
        if line1 != line2:  # 对比两个文件的n行数据
            differ.append(count)    # 两个文件的n行不一样，记录行数
    f1.close()
    f2.close()
    return differ   # 返回differ列表，differ列表存储的是行数

file_one = input("请输入需要比较的头一个文件名：") # 用户输入第一个文件名
file_two = input("请输入需要比较的另一个文件名：") # 用户输入第二个文件名

differ = file_compare(file_one,file_two)    # 调用函数实参

if len(differ) == 0:    # 判断differ，如果里面没有数据，则文件完全一样
    print('两个文件完全一样！')
else:
    print('两个文件共有【%d】处不同：'% len(differ)) # len方法：读取differ的元素个数
    for each in differ: # 迭代取出每个元素
        print('第%d 行不一样' %each) #打印每个元素的数据