#coding=utf-8
import json,os
from web import sina_news_get


def data_web_get():
    user_data_counts_input = input('输入想查询的新闻数量吧：')
    user_want_data_input = input('输入想查询新闻的哪些内容吧（输入代号哦，！不加空格就行（加了就炸）！）,'
                                 '（w：新闻网址，h：新闻标题，k：新闻关键字，t：新闻发布时间，i：新闻概述）(展示顺序跟输入顺序有关哦）：')
    # print(user_want_data_input,type(user_want_data_input))
    user_nwes=sina_news_get(user_data_counts_input,user_want_data_input)
    if user_nwes == -1:
        print('输入的新闻数量或者查询内容的格式不对，炸了，再次启动吧')
        print('输入查寻关键词错误')
        exit(-1)
    obtain_time=user_nwes.pop(0).values()
    print("当前新闻获取时间",":",*obtain_time)
    return user_nwes



def data_local_get():
    file=open('./data/data.txt','r',encoding='utf8')
    data=json.load(file)
    return  data



def __file_name_set():
    while True:
        file_name = input('输入希望得到的数据文件的名字吧（仅仅输入希望文件名即可，文件格式后缀不必输入，默认.txt）：')
        if os.path.exists(f"./{file_name}.txt"):
            print('重名了，请重新输入名字')
        else:
            return f"{file_name}.txt"
def add_id(data:dict,whether):
    already_add = []
    if whether == 'y':
        id=1
        if 'id' not in data[0]:
            for adata in data:
                d=list(adata.items())
                d.insert(0,('id',id))
                data_dict={k:v for k,v in d}
                already_add.append(data_dict)
                id+=1
        else:
            for datas in data:
                datas=datas.copy()
                datas['id']=id
                already_add.append(datas)
                id+=1
    elif whether == 'n':
            already_add.extend(data)
    else:
        return -3
    return already_add

def data_source():
    print('请选择数据来源吧')
    while True:
        choice = input('w：来自即时网路，s：来源本地数据库：')
        if choice == 'w':
            base_data = data_web_get()
            break
        elif choice == 's':
            base_data = data_local_get()
            break
        else:
            print('输错了，没有输入w或s哦')
    return base_data


def data_print(base_data):
    while True:
        user_whether_want_show_data = input('想看具体数据吗？（y/n）')
        if user_whether_want_show_data == 'y':
            file_name=__file_name_set()
            datafile=open(f'./{file_name}','w+',encoding='utf8')
            for data in base_data:
                    for k,v in data.items():
                        print(f"{k}:{v}",end='    ',file=datafile)
                    print('',file=datafile)
            print(f'已经将数据打印至当前路径<{file_name}>')
            break
        elif user_whether_want_show_data =='n':
            break
        else:
            continue
    return base_data


def whether_add_id(data):
    whether=input('获取的数据是否添加id？（y/n）：')
    datas=add_id(data,whether)
    return datas
