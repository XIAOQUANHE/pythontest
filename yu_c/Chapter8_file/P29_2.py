# 2. 编写一个程序，当用户输入文件名和行数（N）后，将该文件的前N行内容打印到屏幕上。
def file_view(file_name,line_num):
    print('\n文件%s的前%s的内容如下：\n'% (file_name,line_num))
    f = open(line_num)
    for i in range(int(line_num)):
        print(f.readline(),end='')

    f.close()

file_name = input(r"请输入要打开的文件（C:\\test.txt）:")
line_num = input('请输入需要显示该文件的前几行：')
file_view(file_name,line_num)