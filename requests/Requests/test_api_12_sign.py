'''
鉴权
1、session-cookies   （安全系数不高）
2、auth 鉴权
3、token
4、sign
5、oauth 鉴权  （很多系统，需要第三方系统授权操作，一般第三方比较多，支付宝，微信，qq，微博，等等）
很多互联网公司，token跟sign差不多
'''
# 举例说明，微信支付sign签名
'''
业务背景：
有一个参数叫 sign，需要值，值怎么来
1、需要前面参数，用ASCII码进行从小到大排序
        appid： wxd930ea5d5a258f4f
        mch_id： 10000100
        device_info： 1000
        body： test
        nonce_str： ibuaiVcKdpRxkhJA

2、排序完成的参数名跟参数值用 &拼接
        appid=wxd930ea5d5a258f4f&body=test&device_info=1000&mch_id=10000100&nonce_str=ibuaiVcKdpRxkhJA
        
3、拼接完成，还需要加入 每个商户key值也需要拼接
        appid=wxd930ea5d5a258f4f&body=test&device_info=1000&mch_id=10000100&nonce_str=ibuaiVcKdpRxkhJA&key=192006250b4c09247ec02edce69f6a2d
4、拼接完成的字符串，进行加密处理，md5加密
        md5的加密
5、生成的md5加密的值，就是我们的sign值
6、填写到我们请求参数 sign 里面
'''
# 如何加密，解决方法
# 1、找网站上面很多在线进行加密
# 2、用python 加密的代码包进行加密 hashlib 包
s = 'appid=wxd930ea5d5a258f4f&body=test&device_info=1000&mch_id=10000100&nonce_str=ibuaiVcKdpRxkhJA&key=192006250b4c09247ec02edce69f6a2d'
import hashlib  # 为了处理数据的加密
md = hashlib.md5() # 构建一个对象，为md
md.update(s.encode())  # 对s 字符串进行编码
# result 生成后加密的值
result = md.hexdigest() # 数据的加密
# 把加密的结果，小写转换成大写 upper 函数
result = result.upper()
print(result)
'''
总结下
1、根据前面参数，进行ASCII排序，拼接key值
2、再通过加密生成sign
3、发送请求 sign 值，添加生成的加密的内容
'''