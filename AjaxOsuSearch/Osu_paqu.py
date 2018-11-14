import requests
import re
def Get_OsuHtml(Osu_numbers):
    print('程序已启动\n正在为您查询数据，请稍后'.center(30))
    url='https://osu.ppy.sh/users/%s'%Osu_numbers
    try:
        response=requests.get(url)
        print(response)#<Response [200]>  200代表成功
        response.encoding='utf-8'
        Osuhtml=response.text#爬取该ID的主页html
        return Osuhtml
    except:
        print('失败')
        return "没东西"