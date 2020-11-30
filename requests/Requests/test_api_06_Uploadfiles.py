# 携程网里面的个人信息，图片上传接口
import requests as rs
# url = 'https://sinfo.ctrip.com/MyInfo/Ajax/UploadPhoto.ashx'
# cookies = {
# 'Cookie': '_abtest_userid=e74947f2-b511-4150-ba43-0989cd2dec8f; Session=smartlinkcode=U130026&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4897&SID=130026&OUID=&createtime=1606186445&Expires=1606791245118; MKT_CKID=1606186445310.3yzm1.7yhb; MKT_CKID_LMT=1606186445311; _ga=GA1.2.1085136182.1606186446; _gid=GA1.2.1399092328.1606186446; ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; MKT_Pagesource=PC; _RF1=116.235.180.243; _RSG=6P4UGhbwxaEm51wfDZTwD9; _RDG=28867b5f8f24bd2c6303069684700fdf57; _RGUID=e93bea5a-d078-4646-937a-763369e81170; cticket=57E09281B56989D50DFCB6A9ED6F2196A7502525F9446201CAF58D25D469B34F; AHeadUserInfo=VipGrade=0&VipGradeName=%C6%D5%CD%A8%BB%E1%D4%B1&UserName=&NoReadMessageCount=0; ticket_ctrip=bJ9RlCHVwlu1ZjyusRi+ypZ7X2r4+yojXN5UTMe2Bf1ySY06xPe78dRRk3VVNaq+abkL5h8MrQBi41eIxP/n6sP/pNY4oRSs4pgZTuONEpAjy3Yrcjz+I/j5fKURt/ZIANPCzg6ubLpfJSgYtY3rci5ZpGcGkL5PY8Pz1fUNFQZfqyRq3E9be+d25RBftoULiTYBdy8G5ypAU8gXkBT8Uaau8eZrf16lvNhzM0V9diiMxepOYdoKcco+SSZaw7NgoHvroeeHW9BLtne7SruyxWdMXHhh6y3G2SdJpLjM6R7LefEiXQ9KpQ==; DUID=u=CEAF8C7D0B63887FB1CD9AE057CF3237100EE517D768140F743C43D16C1AF9D4&v=0; IsNonUser=F; UUID=C20C29D723A14369A7DAE721A1BE605E; IsPersonalizedLogin=F; _gat=1; _jzqco=%7C%7C%7C%7C1606186446617%7C1.1805174747.1606186445262.1606186445263.1606186687697.1606186445263.1606186687697.0.0.0.2.2; __zpspc=9.1.1606186445.1606186687.2%232%7Cwww.baidu.com%7C%7C%7C%7C%23; ASP.NET_SessionSvc=MTAuNjAuMzUuMTQ2fDkwOTB8amlucWlhb3xkZWZhdWx0fDE1ODkwMDMyMjQ5NDI; ASP.NET_SessionId=eifhh3jqez5nutg5ttnqqdqf; MyCtripDescription=UID=19736193E19AF73F3004658959EEBA688E2686EEAC7ABD94&IsClub140=F&IsHoliday=F&CorpMileage=F; _bfa=1.1606186444768.dhq7t.1.1606186444768.1606186444768.1.6; _bfs=1.6; _bfi=p1%3D100013%26p2%3D100021%26v1%3D6%26v2%3D5'
# }
# '''
# 以下参数可以通过抓包进行获取
# 1、uploadFile_85  文件参数的名字
# 2、filename为sleep.jpg 文件名
# 3、open('..\\image\\sleep.jpg','rb')  打开本地的一个文件
# 4、文件格式 image/jpeg
# '''
# files = {
#         'uploadFile_85':('sleep.jpg',open('..\\image\\cat.jpg','rb'),'image/jpeg')
#         }
# r = rs.post(url=url,files=files,cookies=cookies)
# print(r.text)
# 不需要处理按钮，接口直接请求
# 接口测试校验2个地方 1、校验返回的结果是否跟开发定义一致  2、校验下，实际接口产生的逻辑结果是否正确
# 百货商城平台上传头像
import requests as rs
url = 'http://www.bhscpt.com/Front/MemberCenter/savePhoto.html'
cookies = {
'Cookies':'yundu_think_language=zh-CN; PHPSESSID=3fnas0sar7spj2q68n8fou3lo3; yundu_member_auth=gnSjqbJ8eK6ueHndhn2AqIB5sM-C27ChkMybqYbQm2qOhMWpsn-Ar697is6Sa4WYf4ys0IKTt2l5tpeqhrqRbYRxn28'
        }
files = {
        'photo':('cat.jpg',open('../image/cat.jpg','rb'),'image/jpeg')
        }
r = rs.post(url=url,cookies=cookies,files=files)
print(r.text)

