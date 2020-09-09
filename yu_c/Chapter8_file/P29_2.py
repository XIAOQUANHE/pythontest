#2. 编写一个程序，当用户输入文件名和行数（N）后，将该文件的前N行内容打印到屏幕上。
def file_view(file_name,line_num):
    print('\n文件%s的前%s的内容如下：\n'% (file_name,line_num))
    f = open(file_name)
    for i in range(int(line_num)):  # 读取用户输入的行数，进行遍历
        print(f.readline(),end='')  # f.readline读取文件的一行，指针位置改变，根据for语句次数行读取

    f.close()   # 关闭文件

file_name = input(r"请输入要打开的文件（C:\\test.txt）:") # 输入格式需要“//”，不能使用r格式
line_num = input('请输入需要显示该文件的前几行：')
file_view(file_name,line_num)   # 调用函数