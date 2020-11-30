'''
鉴权的token操作，token 也叫令牌，临时身份证，比cookies安全一些，一般都是随机字符加上时间戳生成的
业务规则，登录以后，返回一个token给我们，拿这个token进行后面接口的操作
举例说明-
'token':'e2bd1fd4ea414190801d25610ef5f53c',
'''
#话费充值-查询运营商接口
import requests as rs
url_search = 'https://www.quduofan.com/api/sys/getmobilelocation.php'
params_search = {
    'userid':'77197',
    'token':'e2bd1fd4ea414190801d25610ef5f53c',
    'account':'17688829122'
    }
r = rs.get(url=url_search,params=params_search)
print(r.text)

# 话费充值-提单接口
url_submit = 'https://www.quduofan.com/api/wxminipro/hfpay.php'
params_submit = {
        'userid':77197,
        'token':'',
        'openid':'oU3rI5VTcn9GHTN0Rgvtq1o7VKEY',
        'account':17688829122,
        'amount':10,
        'inprice':9.7,
        'shoptype':12,
        'popid':0,
        'couponid':0,
        'coin':0,
        }
r_submit = rs.get(url=url_submit,params=params_submit)
print(r_submit.text)

'''
问题：重新登录，重新生成token值，用原来的token，提示失败
总结下：
1、需求 登录后，获取前一个接口返回的token
2、后面的接口，添加前面返回的token值
解决token鉴权问题
'''