import string
# 低级密码要求：
# 1、密码由单纯的数字或字母组成
# 2、密码长度小于等于8位
# 中级密码要求：
# 1、密码必须由数字、字母或特殊字符（仅限：~!@#%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
# 2、密码长于不能低于8位
# 高级密码要求：
# 1、密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
# 2、密码只能由字符开头
# 3、密码长度不能低于16位
# 思路：
# 1、isalnum()：如果字符串至少有一个字符并且所有字符都是字母或数字则返回True，否则返回False。
# 2、设置密码强度变量，如符合一个条件+1，以此类推
# 3、定义一个空字符串，用来存储满足条件的内容
passwd = input('请输入需要检查的密码组合：')
length = len(passwd)
strpun = ""
passwd_strong = 0
if length <= 8:
    passwd_strong += 1
if length > 8:
    passwd_strong += 1
for i in passwd:
    if i.isalnum():
        strpun += "1"
    elif i in string.punctuation:
        strpun += "2"
if "1" in strpun:
    passwd_strong += 1
if "2" in strpun:
    passwd_strong += 1
if length >= 16:
    passwd_strong += 1
for i in passwd[:1]:
    if i.isalpha():
        passwd_strong += 1
# passwd_strong == 2 低级
# passwd_strong == 3 中级
# passwd_strong == 5 高级
if passwd_strong == 2:
    print("您的密码安全级别评定为：低\n请按以下方式提升您的密码安全级别：")
    print("\t1.密码必须由数字、字母及特殊字符三种组合\n\t2.密码只能由字母开头\n\t3.密码长度不能低于16位")
elif passwd_strong == 3:
    print("您的密码安全级别评定为：中\n请按以下方式提升您的密码安全级别：")
    print("\t1.密码必须由数字、字母及特殊字符三种组合\n\t2.密码只能由字母开头\n\t3.密码长度不能低于16位")
elif passwd_strong == 5:
    print("您的密码安全级别评定为：高\n请继续保持")

