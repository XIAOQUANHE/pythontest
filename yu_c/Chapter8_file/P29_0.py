# 0 编写一个程序，接受用户的输入并保存为新的文件
def file_write(file_name):
    f = open((r"../test_data/%s"%file_name),'w') # 接收用户输入的文件名，并创建
    print('请输入内容【单独输入\':w\'保存退出】：') # 提示用户输入内容

    while True:
        write_some = input()    # 接收用户输入的内容
        if write_some != ':w':  # 判断用户输入的内容不等于":w"
            f.write('%s\n'% write_some) # 接收用户输入的内容，写入文件里面，写入一次，换行一次
        else:
            break   #判断用户输入的内容等于“:w”，终止循环，终止用户输入
    f.close() # 关闭文件


file_name = input("请输入文件名：") # 接受用户输入文件名
file_write(file_name)   # 调用函数