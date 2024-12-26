#!/usr/bin/python3
#coding=utf-8

import requests, json
import os

SCKEY=os.environ.get('SCKEY') #CoolPush酷推KEY
SKey=os.environ.get('SKEY') ##Server酱推送KEY
def ServerPush(info): #Server酱推送
    api = "https://sctapi.ftqq.com/{}.send".format(SKey)
    title = u"汇率推送"
    content = info.replace('\n','\n\n')
    data = {
        "text": title,
        "desp": content
    }
    print(content)
    response = requests.post(api, data=data)
    print(response.text)
    print('++++++++++++++++++++++')
def CoolPush(info): #CoolPush酷推
    # cpurl = 'https://push.xuthus.cc/group/'+spkey   #推送到QQ群
    # cpurl = 'https://push.xuthus.cc/send/' + SKey  # 推送到个人QQ
    api='https://sctapi.ftqq.com/{}.send'.format(SCKEY)
    print(api)
    print(info)
    requests.post(api, info.encode('utf-8'))
def main():
    try:
        api = 'http://web.juhe.cn/finance/exchange/rmbquot?type&bank=1&key=1b545769e75d78c667ebc4d04491a99c'             #API地址，必须配合城市代码使用
        response = requests.get(api)
        d = response.json()         #将数据以json形式返回，这个d就是返回的json数据
        if(d['resultcode'] == "200"):     #当返回状态码为200，输出天气状况
            item = d["result"][0]["data4"] #日元
            # 天气提示内容
            tdwt = "【今日份汇率】\n日元： " + item["fBuyPri"] + "\n更新时间: " + item["time"] + "\n✁-----------------------------------------\n"
            # print(tdwt)
            # requests.post(cpurl,tdwt.encode('utf-8'))         #把天气数据转换成UTF-8格式，不然要报错。
            ServerPush(tdwt)
#             CoolPush(tdwt)
    except Exception:
        error = '【出现错误】\n　　今日汇率推送错误，请检查服务或网络状态！'
        print(error)
        print(Exception)

if __name__ == '__main__':
    main()

