'''1、如下图，实现一个用于登记用户账号信息的页面（如果是带*号的必填项，要求一定要有输入并且不能是空格）。'''
import easygui as eg
msg = '请填写以下联系方式'
title = "账号中心"
fieldNames = [' *用户名',' *真实姓名',' 固定电话',' *手机号码',' QQ',' *E-mail']
fieldVaules = []
fieldVaules = eg.multenterbox(msg,title,fieldNames)     # multenterbox:多行文本输入框

while 1:
    if fieldVaules == None:
        break
    errmsg = ""
    for i in range(len(fieldNames)):
        option = fieldNames[i].strip()  # strip():默认删除字符串头和尾的空白字符（b包括\n,\r,\t这些）
        if fieldVaules[i].strip() == "" and option[0] == "*":   # 判断必须用户输入的字段是否为空
            errmsg += ('【%s】为必填项。\n\n' % fieldNames[i])
    if errmsg == "":
        break
    fieldVaules = eg.multenterbox(errmsg,title,fieldNames,fieldVaules)

print("用户资料如下：%s" % str(fieldVaules))
