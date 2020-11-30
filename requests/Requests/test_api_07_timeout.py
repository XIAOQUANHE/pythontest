# 导包
import requests as rs
# 介绍下 timeout 参数
'''
1、测试接口的时候，我们除了检查返回的结果，跟业务逻辑是否正确以外，有的还需要要求接口请求返回结果时间在一个范围内
比如说：淘宝查询手机号码的接口，控制在2s以内才算正常
2、测试接口的时候，有些接口请求时间，不固定，比如上传图片接口，控制2s以内，查看是否成功
   轮循，当接口响应时间在2s以内，认为是成功，超过2s，认为是失败
'''
# url_taobao = 'http://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=17688829122'
# r_taobao = rs.get(url=url_taobao,timeout=1)
# print(r_taobao.text)
# 校验时间在一个特定值内才会认为接口返回成功
# 轮循
# 百货商城平台上传头像
for i in range(0,10):
        try:
                url = 'http://www.bhscpt.com/Front/MemberCenter/savePhoto.html'
                cookies = {
                'Cookie':'yundu_think_language=zh-CN; PHPSESSID=3fnas0sar7spj2q68n8fou3lo3; yundu_member_auth=gnSjqbJ8eK6ueHndhn2AqIB5sM-C27ChkMybqYbQm2qOhMWpsn-Ar697is6Sa4WYf4ys0IKTt2l5tpeqhrqRbYRxn28'
                        }
                files = {
                        'photo':('sleep.jpg',open('../image/sleep.jpg','rb'),'image/jpeg')
                        }
                r = rs.post(url=url,cookies=cookies,files=files,timeout=1.2)
                print(r.status_code)
        except:
            print('返回失败')

