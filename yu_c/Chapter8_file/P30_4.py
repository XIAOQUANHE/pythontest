# 4. 编写一个程序，用户输入关键字，查找当前文件夹内（如果当前文件夹内包含文件夹，则进入文件夹继续搜索）所有含有该关键字的文本文件（.txt后缀），
# 要求显示该文件所在的位置以及关键字在文件中的具体位置（第几行第几个字符）
import os

def print_pos(key_dict):
    keys = key_dict.keys()
    keys = sorted(keys)
    for each_key in keys:
        print('关键字出现在第 %s 行，第 %s 个位置。' % (each_key,str(key_dict[each_key])))



def pos_in_line(line,key):
    pos = []            # 创建一个空列表
    begin = line.find(key)      # 字符串中找出某个子字符串第一个匹配项的索引位置，该方法与 index() 方法一样，只不过如果子字符串不在字符串中不会报异常，而是返回-1。
    while begin != -1:          # 条件不等于-1，执行下面的语句
        pos.append(begin + 1)   # 把找到的关键字位置写入pos列表里面；+1是因为索引位置是从零开始
        begin = line.find(key,begin+1)  # 从下一个位置继续查找

    return pos      # 返回关键字的位置



def search_in_file(file_name,key):      # 例如：file_name=D:\code\python\pythontest\yu_c\test_data\record.txt；key还是用户输入的key
    f = open(file_name)     # 打开路径上的.txt文件
    count = 0               # 记录行数
    key_dict = dict()       # 创建一个空字典

    for each_line in f:     # 遍历.txt文件的每一行
        count += 1          # 记录行数
        if key in each_line:    # 用户输入的关键字与之匹配
            pos = pos_in_line(each_line,key)    # 匹配到了就调用pos_in_line函数进一步处理，传一行数据和key
            key_dict[count] = pos

    f.close()
    return key_dict


def search_files(key,detail):               # 接收实参
    all_files = os.walk(os.getcwd())        #os.walk：遍历该目录下的所有文件，返回一个三元组(root,dirs,files)
    txt_files = []                          # 声明一个空列表

    for i in all_files:                     # 解析：for(root,dirs,files) in os.walk(os.getcwd())
        for each_file in i[2]:              # 遍历当前目录下的所有文件
            if os.path.splitext(each_file)[1] == '.txt':    # 分离文件名与扩展名；[1]取扩展名匹配
                each_file = os.path.join(i[0],each_file)    # join:将path1，path2各部分合成一个路径；i[0]=root：所指的是当前正在遍历的这个文件夹的本身的地址
                # 上一行代码中的 each_file 符合.txt的文件名;例如：D:\code\python\pythontest\yu_c\test_data\OpenMe.txt
                txt_files.append(each_file) # 录进txt_files这个列表

    for each_txt_file in txt_files:         # 遍历txt_files这个列表，列表存储的是符合.txt的路径
        key_dict = search_in_file(each_txt_file, key)   # 把每一条符合.txt的路径传给serch_in_file这个函数进行处理
        if key_dict:
            print('==================================================')
            print('在文件【%s】中找到关键字【%s】' % (each_txt_file, key))   # 打印文件路径和用户输入的关键字
            if detail in ['YES', 'Yes', 'yes']:     # 交互用户输入的是yes
                print_pos(key_dict)                 # 打印key_dict,也就是关键出现在某行


key = input('请将该脚本放于待查找的文件夹内，请输入关键字：')              # 程序开始的地方，请用户输入
detail = input('请问是否需要打印关键字【%s】在文件中的具体位置(YES/NO):'% key)    # 交互性
search_files(key,detail)            # 调用函数，传用户输入的关键字和交互信息

