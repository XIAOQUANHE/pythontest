'''
session 参数
有很多接口需要一些公共的参数，比如cookies
百货商城平台(都有公共的参数cookies值)  通过登录生成
1、添加地址
2、文件上传的接口
建立三个接口，登录接口、添加地址接口、文件上传接口
'''
import requests as rs
import time
# 1、登录接口
url_login = 'http://www.bhscpt.com/Front/Login/login.html'
data_login = {
            'username':'spring',
            'password':123456
            }
cookies_login = {
                'cookies':'PHPSESSID=3fnas0sar7spj2q68n8fou3lo3'
                }
sn = rs.session()
r_login = sn.post(url=url_login,data=data_login)
print(r_login.encoding)
print(r_login.content.decode('unicode_escape')) # unicode-escape编码集，他是将unicode内存编码值直接存储

# 2、添加地址接口
url_addarea = 'http://www.bhscpt.com/Front/Member/saveAddress.html'
# 工作当中，如果接口需要哪些cookies值，咨询后端开发人员，此接口只需要PHPSESSID参数
cookies_addarea = {
        'PHPSESSID':'3fnas0sar7spj2q68n8fou3lo3'    # 验证用户信息
        }
data_addarea = {
        'province':'25',
        'city':'3413',
        'zone':'2708',
        'address':'阿西吧城',
        'realname':'河蟹',
        'phone': '17177779835',
        'tel':'',
        'zipcode':'',
        'is_default': 1
        }
# 提示“还不是商城用户”,要先登录，如果直接添加成功，就是一个bug
# 问题，没有携带用户辨明信息，cookies
r_addarea = sn.post(url=url_addarea,data=data_addarea)
print(r_addarea.encoding)
print(r_addarea.content.decode('unicode_escape'))  # 先把返回的结果转换城utf-8，再去解码成中文编码

time.sleep(2)
# 3、文件上传接口（上传头像）
url = 'http://www.bhscpt.com/Front/MemberCenter/savePhoto.html'
cookies = {
'Cookies':'yundu_think_language=zh-CN; PHPSESSID=3fnas0sar7spj2q68n8fou3lo3; yundu_member_auth=gnSjqbJ8eK6ueHndhn2AqIB5sM-C27ChkMybqYbQm2qOhMWpsn-Ar697is6Sa4WYf4ys0IKTt2l5tpeqhrqRbYRxn28'
        }
files = {
        'photo':('cat.jpg',open('../image/cat.jpg','rb'),'image/jpeg')
        }
r = sn.post(url=url,files=files)
print(r.text)

'''
如何去把公共的参数保存在session里面
操作步骤：
1、步骤 建立session，名字随意，sn sn = requests.session
2、后续的请求中，直接用sn去发送请求，把requests替换成sn
3、公共参数已经保存到sn里面，添加地址接口与文件上传接口中，去掉cookies请求
'''