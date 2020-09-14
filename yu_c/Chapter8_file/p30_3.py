# 3. 编写一个程序，用户输入开始搜索的路径，查找该路径下（包含子文件夹内）所有的视频格式文件（要求查找mp4 rmvb, avi的格式即可），
# 并把创建一个文件（vedioList.txt）存放所有找到的文件的路径
import os       # 导入os模块

def search_file(start_dir,target):                  # 接口实参
    os.chdir(start_dir)                             # 切换到用户输入的目录


    for each_file in os.listdir(os.curdir):         # os.listdir()列举指定目录中的文件名,os.curdir：指代当前目录
        ext = os.path.splitext(each_file)[1]        # 分离文件名与扩展名，[0]是文件名，[1]是扩展名
        if ext in target:                           # ext存储的时扩展名，与列表进行匹配
            vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)    # 符合条件，往vedio_list列表里面存储目录地址
        if os.path.isdir(each_file):                # 判断指定路径是否存在且是一个目录
            search_file(each_file,target)           # 是的话，递归调用函数
            os.chdir(os.pardir)                     # os.chdir:指代当前目录; os.pardir: 指代上一级目录

start_dir = input('请输入待查找的初始目录：')       # 用户输入初始目录
program_dir = os.getcwd()                         # 记录当前工作目录

target = ['.mp4', '.avi', '.rmvb']                # 需要查找的文件后缀名
vedio_list = []                                   # 定义一个列表，为后面符合target的数据存储

search_file(start_dir,target)                     # 调用search_file函数

f = open(program_dir + os.sep + 'vediolist.txt','w')    # 当函数调用完了之后，创建一个.txt文件
f.writelines(vedio_list)                                # 把vedio_list列表里面的值写进.txt文件中
f.close()                                               # 关闭文件