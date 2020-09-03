#       *****编写一个用户登录程序（这次尝试将功能封装成函数）*****
# 全局字典
user_data = {}

# 新建用户
def new_user():
    prompt = '请输入用户名：'
    while True:
        name = input(prompt)
        if name in user_data:   # name存在，continue
            prompt = '此用户名已经被使用，请重新输入：'
            continue
        else:
            break
    passwd = input('请输入密码：')
    user_data[name] = passwd
    print('注册成功，赶紧试试登录吧^_^')
    print(user_data)

# 登录用户
def old_user():
    prompt = '请输入用户名：'
    while True:
        name = input(prompt)
        if name not in user_data:   # aaa not in aaa中，结束循环
            prompt = '您输入的用户名不存在，请重新输入：'
            continue
        else:
            break

    passwd = input('请输入密码：')
    pwd = user_data.get(name)   # 通过key找到value
    if passwd == pwd:
        print('欢迎进入何小泉开发系统，请点击右上角的X结束程序！')
    else:
        print('密码错误！')

def showmenu():
    prompt = ''' 
    |--- 新建用户：N/n ---|
    |--- 登录账号：E/e ---|
    |--- 退出程序：Q/q ---|
    |--- 请输入指令代码：'''

    while True:
        chosen = False
        while not chosen:           # 当chosen为真时，结束该循环
            choice = input(prompt)  # 每次输入错误，都会打印prompt的内容
            if choice not in 'NnEeQq':  # 验证输入指令代码是否正确
                print('您输入的指令错误，请重新输入')
            else:
                chosen = True
        if choice == 'q' or choice == 'Q':
            break
        if choice == 'e' or choice == 'E':
            old_user()
        if choice == 'n' or choice == 'N':
            new_user()

showmenu()