import requests

FromData={}
FromData['i']='Hello'
FromData['from']='AUTO'
FromData['to']='AUTO'
FromData['smartresult']='dict'
FromData['client']='fanyideskweb'
FromData['salt']='15739126086498'
FromData['sign']='a54a59a18a6014fc8d948dc83041a872'
FromData['ts']='1573912608649'
FromData['bv']='75551116684a442e8625ebfc9e5af1ba'
FromData['doctype']='json'
FromData['version']='2.1'
FromData['keyfrom']='fanyi.web'
FromData['action']='FY_BY_REALTlME'


URL="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
response =requests.post(URL,data=FromData,headers=header)
#print(response.text)

res_json = response.json()
print("翻译结果为: ",res_json['translateResult'][0][0]['tgt'])
