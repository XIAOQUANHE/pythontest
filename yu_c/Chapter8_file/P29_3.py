# 3.呃，不得不说我们的用户变得越来越刁钻了。要求在上一题的基础上扩展，用户可以随意输入需要显示的行数。
# （如输入13:21打印第13行到第21行，输入:21打印前21行，输入21:则打印从第21行开始到文件结尾所有内容）
def file_view(file_name,line_num):
    #用户输入的是冒号，去除前后空格，给两个变量赋值
    if line_num.strip() == ':': # strip 删除字符串前边和后边所有的空格
        begin = '1'
        end = '-1'

    (begin,end) = line_num.split(':') # 以冒号为分割符，begin为xx:的值，end为:xx的值
    # split(sep=None, maxsplit=-1)不带参数默认是以空格为分隔符切片字符串，如果maxsplit参数有设置
    # 则仅分隔maxsplit个子字符串，返回切片后的子字符串拼接的列表。
    if begin == '':
        begin = '1'
    if end == '':
        end = '-1'

    if begin == '1' and end == '-1':
        prompt = '的全文'
    elif begin == '1':
        prompt = '从开始到%s' % end
    elif end == '-1':
        prompt = '从第%s到结束' % begin
    else:
        prompt = '从第%s行到第%s行' % (begin,end)

    print('\n文件%s%s的内容如下：\n'% (file_name,prompt))
    begin = int(begin) - 1
    end = int(end)
    lines = end - begin
    f = open(file_name)

    for i in range(begin):  # 用于消耗掉begin之前的内容,但是上面进行begin-1操作，所以消耗行数-1
        print(f.readline())

    if lines < 0:   # lines小于0，除去消耗掉begin的内容，余下的内容全部打印出来
        print(f.read())     # 减去消耗的行数内容，read打印文件全部内容
    else:
        for j in range(lines):
            print(f.readline(),end= '')

    f.close()

file_name = input(r"请输入要打开的文件（C:\\test.txt）:")
line_num = input(r"请输入需要显示的行数【格式如 13:21 或 :21 或 21: 或 :】：")
file_view(file_name,line_num)   # 调用函数