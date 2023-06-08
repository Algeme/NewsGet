#coding:utf-8

from data.data_sort import bubble_sort, __compear_data
import re

def data_test(f):
    def test(data):
        try:
            len(data)
        except:
            return -6
        else:
            datas=data.copy()
            return f(datas)
        finally:
            del datas
    return test
def __not_vally(data,keyword):
    try:
        data[0][keyword]
    except :
        print('关键字输入错误，获取的信息信息中没有该关键字哦！')
        return True


def half_find(data:list,keyword:str,want_find):
    try:
        len(data)
    except:
        return -6
    data = bubble_sort(data, keyword=keyword, reverse=False)
    left = 0
    right = len(data)
    while True:
        middle = (left + right) // 2
        if left != right:
            if __compear_data(data[middle][keyword],keyword)>= __compear_data(want_find,keyword):
                right = middle - 1

            elif __compear_data(data[middle][keyword],keyword)<= __compear_data(want_find,keyword):
                left = middle + 1

            else:
                return data[middle]
        else:
            if __compear_data(data[middle][keyword],keyword) == want_find:
                return data[middle]
            return -4

@data_test
def data_keywors_get(data):
    keyword=input('请输入想查询的关键词：')
    find_data=[]
    for adata in data:
        if re.fullmatch(r'.*(%s).*'%keyword,str(adata)):
            find_data.append(adata)
    if len(find_data)==0:
        return -4
    return find_data


@data_test
def data_keywords_get_count(data):
    d=data_keywors_get(data)
    try:
        len(data)
    except:
        return -6
    else:
        print( len(d))
        return 1

@data_test
def data_timekeywords_get(data):
    if __not_vally(data,'新闻时间'):
        return -1
    p_data=[]
    try:
        begin_time=list(map(int,input('开始时间（格式：年 月 日 时 分 秒），例：2023 06 01 13 00 00').split()))
        end_time = list(map(int, input('结束时间（格式：年 月 日 时 分 秒）').split()))
        data=bubble_sort(data,keyword='新闻时间',reverse=False)
        flug=0
        for adata in data:
            if __compear_data(adata['新闻时间']) > __compear_data(f'{begin_time[0]}-{begin_time[1]}-{begin_time[2]} {begin_time[3]}:{begin_time[4]}:{begin_time[5]}') \
            and __compear_data(adata['新闻时间']) < __compear_data(f'{end_time[0]}-{end_time[1]}-{end_time[2]} {end_time[3]}:{end_time[4]}:{end_time[5]}'):
                flug=1
                p_data.append(adata)
        if flug==1:
            return p_data
        else:
            return -4
    except:
        return -3

# print(data_timekeywords_get(a))

@data_test
def data_section_get(data):
    begin=input('输入开始的标号吧')
    if re.match(r'\D', begin):
        return -3
    begin=int(begin)-1
    end=input('输入结束的标号吧')
    if re.match(r'\D', end):
        return -3
    end=int(end)
    if end > len(data):
        return -2
    return data[begin:end]

@data_test
def get_id(data):
    want_id=input('请输入想查询的id')
    if re.match(r'\D', want_id):
        return -3
    want_id=int(want_id)
    if __not_vally(data,'id'):
        return -1
    if int(want_id) > len(data):
        return -2
    return  [half_find(data,'id',want_id)]


