# 4. 编写一个程序，实现“全部替换”功能
def file_replace(file_name,rep_word,new_word):
    f_read = open(file_name)

    content = []
    count = 0

    for eachline in f_read: # 遍历整个文件
        if rep_word in eachline:    # 遍历整行
            count = eachline.count(rep_word)    #.count(sub)返回 sub 在字符串里边出现的次数
            # replace(old, new[, count])——>把字符串中的 old 子字符串替换成 new 子字符串，如果 count 指定，则替换不超过 count 次。
            eachline = eachline.replace(rep_word,new_word)
        content.append(eachline)    #文件每行文字，未经过处理或者经过处理的数据，都存进content列表
    decide = input('\n文件 %s 中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【YES/NO】：'\
                   % (file_name,count,rep_word,new_word))   #输出格式

    if decide in ['YES','Yes','yes']:
        f_write = open(file_name,'w')
        f_write.writelines(content)
        f_write.close()

    f_read.close()


file_name = input('请输入文件名：')
rep_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')
file_replace(file_name,rep_word,new_word)