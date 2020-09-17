'''0. 编写一个程序，这次要求使用pickle将文件record.txt里的对话按照以下要求腌制成不同文件
● 小甲鱼的对话单独保存为boy_*.txt的文件（去掉“小甲鱼:”）
● 小客服的对话单独保存为girl_*.txt的文件（去掉“小客服:”）
● 文件中总共有三段对话，分别保存为boy_1.txt, girl_1.txt，boy_2.txt, girl_2.txt, boy_3.txt, gril_3.txt共6个文件
（提示：文件中不同的对话间已经使用“==========”分割）'''

import pickle

def save_file(boy,girl,count):      # 接收已有数据的boy，girl，count值
    file_name_boy = '../test_data/pickle_data/boy_' + str(count) + '.txt'    # boy文件创建规则拼接
    file_name_girl = '../test_data/pickle_data/girl_' + str(count) + '.txt'  # girl文件创建规则拼接

    boy_file = open(file_name_boy,'wb')     # 记得一定要加 b 吖；创建boy文件，以写入和二进制形式
    girl_file = open(file_name_girl,'wb')   # 记得一定要加 b 吖；创建girl文件，以写入和二进制形式

    pickle.dump(boy,boy_file)               # 把boy的数据存进创建的文件中 dump('obj','file')，必须为write()接口
    pickle.dump(girl,girl_file)             # 把girl的数据存进创建的文件中 dump('obj','file')，必须为write()接口

    boy_file.close()                        # 关闭boy文件
    girl_file.close()                       # 关闭girl文件


def split_file(file_name):          # 接收实参
    count = 1                       # 定义变量count为1，主要记录为等于号的行数
    boy = []                        # boy空列表
    girl = []                       # girl空列表

    f = open(file_name)             # 打开传输过来的文件

    for each_line in f:             # 遍历文件，以行为单位
        if each_line[:6] != '======':   # 判断行的前六个字符是否匹配“等于号”
            (role,line_spoken) = each_line.split(':',1)     # 以冒号分割，只分割一次，冒号前的数据给role，后的给line_spoken
            if role == '小甲鱼':       # 判断
                boy.append(line_spoken) # 追加
            if role == '小客服':       # 判断
                girl.append(line_spoken)    # 追加
        else:
            save_file(boy,girl,count)       # 条件匹配等于号后，走此逻辑；把记录的boy，girl，count值传给下一个函数

            boy = []                        # 处理完后，boy和girl重新定义为空列表
            girl = []                       # 同上
            count += 1                      # count累加

    save_file(boy,girl,count)           # 原数据有三段对话，但只有两条等于线，当for遇到空行的时候，结束了，就走该函数
    f.close()                           # 与for同列，for循环结束后，才运行这两条语句

split_file(r'../test_data/record.txt')          # 调用函数，把文件以实参的形式传输
