'''4. 写一个程序统计你当前代码量的总和，并显示离十万行代码量还有多远？
    要求一：递归搜索各个文件夹
    要求二：显示各个类型的源文件和源代码数量
    要求三：显示总行数与百分比'''
import easygui as eg
import os
def show_result(start_dir):
    lines = 0
    total = 0
    text = ""

    for i in source_list:
        lines = source_list[i]
        total += lines
        text += "%s源代码 %d 个, 源代码 %d 行\n" %(i, file_list[i],lines)
    title = '统计结果'
    msg = '您目前共累计编写了 %d 行代码，完成进度：%.2f %%\n离10万行代码还差 %d 行，请继续努力！'%(total,total/1000,100000-total)
    eg.textbox(msg,title,text)

def calc_code(file_name):   # 把文件
    lines = 0
    with open(file_name) as f:
        print('正在分析文件：%s ...' % file_name)
        try:
            for each_line in f:
                lines += 1
        except UnicodeDecodeError:
            pass # 不可避免会遇到格式不兼容的文件，这里忽略掉......
    return lines

def search_file(start_dir):     # 该函数接收实参，以形参方式进行代入函数
    os.chdir(start_dir)         # chdir:改变工作目录(定位到用户输入的目录)

    for each_file in os.listdir(os.curdir):     # 遍历当前目录下的文件名
        ext = os.path.splitext(each_file)[1]    # 分离文件名和扩展名，[0]返回:f_name [1]返回:f_extension
        if ext in target:       # 找出符合target列表中的文件
            lines = calc_code(each_file) # 统计行数，跳转calc_code函数进一步处理
            # 还记得异常处理的用法吗？ 如果字典中不存，抛出KeyError，则添加字典键
            # 统计文件数
            try:
                file_list[ext] +=1
            except KeyError:
                file_list[ext] = 1
            # 统计源代码行数
            try:
                source_list[ext] += lines
            except KeyError:
                source_list[ext] = lines
        if os.path.isdir(each_file):
            search_file(each_file) # 递归调用
            os.chdir(os.pardir) # 递归调用后切记返回上一层目录

target = ['.c','.cpp','.py','.cc','.java','.pas','.asm']    # 定义后缀名
file_list = {}      # 创建空字典
source_list = {}    # 创建空字典

eg.msgbox("请打开您存放所有代码的文件夹......","统计代码量")   # 提示弹窗
path = eg.diropenbox("请选择您的代码库：")                   # 返回选择目录的绝对路径(完整路径)

search_file(path)       # 把获取到的绝对路径做实参传输
show_result(path)       # 把获取到的绝对路径做实参传输