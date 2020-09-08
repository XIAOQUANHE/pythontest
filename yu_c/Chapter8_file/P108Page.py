def save_file(boy,girl,count):
    # 第一次调用：等号前的数据，boy->小甲鱼说的话，girl->小客服说的话，count=1
    # 第二次调用：第二个等号前的数据，boy->小甲鱼说的话，girl->小客服说的话,count=2
    # 第三次调用，单独调用，不依赖等号取值
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'

    boy_file = open((r"../test_data/%s" % file_name_boy),'w') # 1-> 创建boy_1.txt
    girl_file = open((r"../test_data/%s" % file_name_girl),'w') # 1-> 创建girl_1.txt

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()

def split_file(file_name):
    count = 1
    boy = []
    girl = []
    f = open(file_name)

    for each_line in f:
        if each_line[:6] != '======':
            (role,line_spoken) = each_line.split(':',1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            save_file(boy,girl,count)

            boy = []
            girl = []
            count += 1
    save_file(boy,girl,count)
    f.close()

split_file(r"../test_data/record.txt")
