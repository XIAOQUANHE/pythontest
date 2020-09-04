boy = []
girl = []
count = 1

f = open(r"../test_data/record.txt")

for each_line in f:
    # 取出数据，进行分割，分类存储
    if each_line[:6] != '======':
        (role, line_spoken) = each_line.split(':',1)    # split 字符串中以某个字符截断，1代表分割次数
        if role == '小甲鱼':
            boy.append(line_spoken)
        if role == '小客服':
            girl.append(line_spoken)
    else:
    # 设置文件名称
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'
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

boy_file.close()
girl_file.close()
f.close()
