
#coding:utf-8
import time
import requests
import json
import re

class Requirement_set:
    '''
    这里面存的是用户需要内容的方法，其中函数形参解释如下：
    nwes：指的是用户目标要求的最终新闻集——>dict
    item：网页端获取的独条数据——>dict
    '''
    @staticmethod
    def user_want_web(nwes,item):
        nwes['网址'] = item['url']
    @staticmethod
    def user_want_title(nwes,item):
        nwes['标题'] = item['title']
    @staticmethod
    def user_want_keywords(nwes,item):
        nwes['关键词'] = item['keywords']
    @staticmethod
    def user_want_time(nwes,item):
        nwes['新闻时间'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(item['ctime'])))
    @staticmethod
    def user_want_intro(nwes,item):
        nwes['新闻概述'] = item['intro']

class User_require:
    _user_require = {'w':Requirement_set.user_want_web,
                    'h':Requirement_set.user_want_title,
                    'k':Requirement_set.user_want_keywords,
                    't':Requirement_set.user_want_time,
                    'i':Requirement_set.user_want_intro}
    def __init__(self,item,user_wan_require='ht'):
        self._nwes={}
        self.item=item
        self.user_want_require=user_wan_require

    def add_nwes(self):
        for i in self.user_want_require:
            if i in self._user_require:
                self._user_require[i](self._nwes,self.item)
        return self._nwes

def sina_news_get(data_counts,user_want_data):
    '''

    :param data_counts: 用户希望的数据量
    :param user_want_data: 用户希望的关键词
    :return: 根据用户输入的关键词，选择信息
    '''
    if re.match(r'\D',data_counts) or re.search(r'[^whkti]',user_want_data):
        return -1
    user_want_nwes=[]
    page=1
    while True:
        url = f"https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page={page}"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        if page==1:
            user_want_nwes.append({'当前获取新闻时间':data['result']['timestamp']})
        for item in data['result']['data']:
            if 'url' in item and 'title' in item and 'keywords' in item and 'ctime' in item and 'intro' in item:
                nwes=User_require(item,user_want_data)
                user_want_nwes.append(nwes.add_nwes())
            if len(user_want_nwes)-1 == int(data_counts):
                return user_want_nwes
        else:
            page+=1




