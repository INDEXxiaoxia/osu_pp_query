import urllib
from getOsu.Osu_paqu import *

def Get_OSUlist(html):
    Jiiuzilc=re.findall('{"id":(.*?),"username":"(.*?)","join_date":"(.*?)","country":{"code":"(.*?)"',html)
    Tbxd=re.findall('avatar_url":"(.*?)"',html)
    Leval=re.findall('level":{"current":(.*?),"progress":(.*?)},',html)
    Rank=re.findall('"pp":(.*?),"pp_rank":(.*?),"ranked_score":(.*?),"hit_accuracy":(.*?),"play_count":(.*?),"',html)
    Scorerank=re.findall('"grade_counts":{"ss":(.*?),"ssh":(.*?),"s":(.*?),"sh":(.*?),"a":(.*?)},"rank":{"global":(.*?),"country":(.*?)},',html)
    try:
        #上面是提取，下面是整合
        TJ=Jiiuzilc[0]
        TL=Leval[0]#leval
        TR=Rank[0]#pp
        TS=Scorerank[0]#ss,ssh
        numID,userID,addTime,Cou=TJ[0],TJ[1],TJ[2],TJ[3]
        sadd='''
---------------------------------------------
        用户名--------- %s
        注册时间------- %s
        国家----------- %s
        等级----------- %s(%s%%)
        PP积分--------- %s
        Ranked谱面总分- %s
        ACC正确率------ %s
        PC游戏次数----- %s
----------------累计成绩评级----------------
           ss:%s     ssh:%s
           s :%s     sh :%s
           a :%s
             全球排名:%s
             国内排名:%s
--------------------------------------------
        '''%(userID,addTime,Cou,TL[0],TL[1],TR[0],TR[2],TR[3],TR[4],TS[0],TS[1],TS[2],TS[3],TS[4],TS[5],TS[6])
        dict0={}
        dict0['用户名'],dict0['注册时间'],dict0['国家'],dict0['等级'],dict0['%'],\
        dict0['pp'],dict0['rank分'],dict0['ACC'],dict0['pc'],dict0['ss'],dict0['ssh'],\
        dict0['s'],dict0['sh'],dict0['a'],dict0['全球'],dict0['国内']\
            =userID,addTime,Cou,TL[0],TL[1],TR[0],TR[2],TR[3],TR[4],TS[0],TS[1],TS[2],TS[3],TS[4],TS[5],TS[6]
    except:
        dict0=None
    return dict0
# HTMLOSU=Get_OsuHtml(12223813)
# SSSSOSU=Get_OSUlist(HTMLOSU)
# print(SSSSOSU)