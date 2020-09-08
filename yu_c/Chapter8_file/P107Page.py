# 对一个文件进行操作步骤
# 1、定义三个变量——>打开目标文件“record.txt”，进行读取目标文件
boy = []
girl = []
count = 1

f = open(r"../test_data/record.txt")

for each_line in f:
    #print(each_line) # 调试，for each_line in f 是取目标文件一行
    # 取出数据，进行分割，分类存储
    if each_line[:6] != '======':
        (role, line_spoken) = each_line.split(':',1)    # split 字符串中以某个字符截断，1代表分割次数
        #print(role,line_spoken)  #调试，role取冒号之前的数据，line_spoken是取冒号之后的数据
        if role == '小甲鱼':
            boy.append(line_spoken) # append():boy列表后追加line_spoken数据
        if role == '小客服':
            girl.append(line_spoken)# append():boy列表后追加line_spoken数据
    else:
    # 设置文件名称
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'
        #print(file_name_boy,file_name_girl) # 调试，能生成几个文件名称，生成四个
    # 以文件名来创建文件
        boy_file = open(r"../test_data/"+file_name_boy,'w')
        girl_file = open(r"../test_data/"+file_name_girl,'w')
    # 分割的数据分三次存储
        boy_file.writelines(boy)
        girl_file.writelines(girl)

    # 根据count来进行分别存储
        boy = []
        girl = []
        count += 1
# 运行下来，只能保存两次，因为原文件里面只有两列“======”，判断只能保存两次，需要再次调用一次
file_name_boy = 'boy_' + str(count) + '.txt'
file_name_girl = 'girl_' + str(count) + '.txt'
# print(file_name_boy,file_name_girl) # 调试：文件名补齐，共6个文件名

boy_file = open((r"../test_data\%s" % file_name_boy),'w') # 创建文件名为boy_3.txt
girl_file= open(r"../test_data\%s"  % file_name_girl,'w') # 创建文件名为girl_3.txt

#最后一次存储的数据
boy_file.writelines(boy)    # writelines
girl_file.writelines(girl)

#关闭所有打开的文件
boy_file.close()
girl_file.close()
f.close()
