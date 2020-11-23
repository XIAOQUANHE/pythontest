#请求参数中添加cookies信息
# 举例说明：添加地址的接口
'''
接口信息：
url: http://www.bhscpt.com/Front/Member/saveAddress.html
请求参数:
province: 25
city: 3413
zone: 2708
address: 阿西吧城
realname: 河蟹
phone: 17177779835
tel:
zipcode:
is_default: 1
请求方式:post请求
返回结果:
记住公司里面直接跟开发要接口文档（尽量不要抓包，很多时候前端界面是没有开发完成的，无法实现抓包）
'''
import requests as rs
url = 'http://www.bhscpt.com/Front/Member/saveAddress.html'
# 工作当中，如果接口需要哪些cookies值，咨询后端开发人员，此接口只需要PHPSESSID参数
cookies = {
        'PHPSESSID':'87p72r6p1mi8kdsgviln51tcc0'    # 验证用户信息
        }
data = {
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
r = rs.post(url=url,data=data,cookies=cookies)
print(r.encoding)
print(r.text.encode('utf-8').decode('unicode_escape'))  # 先把返回的结果转换城utf-8，再去解码成中文编码