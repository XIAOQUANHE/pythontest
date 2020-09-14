# 2. 编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在。如遇到文件夹，则进入文件夹继续搜索，程序实现如图
import os

def search_file(start_dir,target):
    os.chdir(start_dir)                                 # os.chdir 改变工作目录，修改成用户输入的目录

    for each_file in os.listdir(os.curdir):             # 遍历当前目录
        if each_file == target:                         # 对比遍历数据是否为用户目标数据
            print(os.getcwd() + os.sep + each_file)     # 使用os.sep使程序更标准，路径分隔符
        if os.path.isdir(each_file):                    # isdir：判断指定路径是否存在且是一个目录
            search_file(each_file,target)               # 如果是一个目录，递归调用函数
            os.chdir(os.pardir)                         # 递归调用后切记返回上一层目录

start_dir = input('请输入待查找的初始目录：')            # D:\code\python\pythontest\yu_c\test_data
target = input('请输入需要查找的目标文件：')             # 0.jpg
search_file(start_dir,target)