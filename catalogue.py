#coding:utf-8
import sys
from data.data_sort import *
from data.data_get import *
from data.data_find import *

class Type_error:
    @staticmethod
    def normal():
        return  True
    @staticmethod
    def keyword_error():
        print('关键词输入错误')
        return False
    @staticmethod
    def input_error():
        print('输入错误')
        return False
    @staticmethod
    def notfind_error():
        print('未找到')
        return False
    @staticmethod
    def range_error():
        print('范围输入错误')
        return False
    @staticmethod
    def error():
        return False
    @staticmethod
    def data_error():
        print('数据错误,请检查数据情况')
    @staticmethod
    def error_dict(data):
        error={'1':Type_error.normal,
               '-1':Type_error.keyword_error,
               '-3':Type_error.input_error,
               '-4':Type_error.notfind_error,
               '-2':Type_error.range_error,
               '-5':Type_error.error,
               '-6':Type_error.data_error}
        if type(data)== int:
            data = str(data)
            if data in error:
                error[data]()
        else:
            return data

class Catalogue:
    def __init__(self):
        self.__database=[]

    def __database_state(self):
        if len(self.__database)==0:
            return False
        return  True
    def __database_get(self):
        if self.__database_state():
            return self.__database[-1]
        else:
            return -4
    def __database_remove(self):
        if len(self.__database)>1:
            return  self.__database.pop(-1)
        else:
            return -4

    def __database_enter(self,data):
        self.__database.append(data)

    def __reverses(self):
        while True:
            k = {'t': False, 'f': True}
            reverse = input('输入正序（t）还是逆序（f）：')
            if reverse in k:
                return k[reverse]
            else:
                print('输入错误，请重新输入')


    def sort(self):
        choice=input('选择排序方式吧：（b,冒泡排序，h，堆排序，m,魔法排序（这个魔法排序支持多关键字排序，全中文输入,包括标点））')
        sort_way={'b':bubble_sort,'h':heap_sort,'m':magic_sort}
        keywords=input('输入要排序的关键字：')
        reverse=self.__reverses()
        if reverse == -3:
            print('输入错误')
            return -3
        if choice in sort_way:
            sort_data=sort_way[choice](self.__database_get(),keywords,reverse)
            if sort_data == -1:
                print('输入关键词错误')
                return  -1
            else:
                self.__database_enter(sort_data)
                print('排序完毕')
                return 1
        else:
            print('输入排序方法错误')
            return -3

    def find(self):
        print('t:找前几的数据，sg,标号范围查找，tg，时间范围查找，gi：获得指定id，kg：关键字查询，kgc：包含关键字的新闻数量')
        choice=input('选择查找方式吧')
        find_way1={'sg':data_section_get,'tg':data_timekeywords_get,'gi':get_id,'kg':data_keywors_get}
        if choice in find_way1:
            data=find_way1[choice](self.__database_get())
            data_error_test=Type_error.error_dict(data)
            if data_error_test:
                self.__database_enter(data_error_test)
                print('查找完毕，已放入数据库')
                return 1
            else:
                return -5
        if choice == 't':
            topn=int(input('输入想查询前几的数据：'))
            keywords=input('输入要查询的关键字：')
            reverse = self.__reverses()
            get_topn=partial_sort(self.__database_get(),topn,keywords,reverse)
            get_topn_error_test=Type_error.error_dict(get_topn)
            if get_topn_error_test:
                self.__database_enter(get_topn_error_test)
                print('查找完毕，已放入数据库')
                return 1
            else:
                return -5
        if choice == 'kgc':
            get=data_keywords_get_count(self.__database_get())
            get_id_error_test=Type_error.error_dict(get)
            if get_id_error_test:
                print(get_id_error_test)
                return 1
            else:
                return -5
        else:
            return -3

    def data_base(self):
        if_data=input('是否需要数据？（y/n）')
        if if_data == 'y':
            d_s=data_source()
            w_a_i=whether_add_id(d_s)
            d_p=data_print(w_a_i)
            d_p_error_test=Type_error.error_dict(d_p)
            if d_p_error_test:
                self.__database_enter(d_p_error_test)
                return 1
            else:
                return -5
        else:
            print('Good Bye,Thank you')
            exit(1)

    def print_data(self):
        data=self.__database_get()
        if  len(self.__database)==1:
            whether=input('数据只有初始数据文件，是否打印？（y/n）：')
            if whether == 'y':
                data_print(self.__database[0])
            elif whether == 'n':
                print('请继续操作')
            else:
                print('输入错误')
        else:
            data_print(data)

    def data_add_id(self):
        a_i=add_id(self.__database_get(),'y')
        a_i_error_test=Type_error.error_dict(a_i)
        if a_i_error_test:
            self.__database_enter(a_i_error_test)
            print('添加完毕')
            return 1
        return -5

    def last_step(self):
        if  self.__database_remove()== -4:
            print('获取失败，数据只有初始数据文件')
        else:
            print('操作已完成')
            return 1

    def data_exits(self):
        self.__database.clear()
        del self.__database
        print('期待下次使用')
        sys.exit(0)

    def show(self):
        data=self.__database_get()
        if data == -4:
            print(f'当前数据表情况为：{self.__database}','缺少数据文件')
            return -4
        else:
            print(data)
            return 1

def catalogue():
    data_operation=Catalogue()
    data_operation.data_base()
    operation={'f':data_operation.find,'s':data_operation.sort,'e':data_operation.data_exits,'p':data_operation.print_data,'r':data_operation.last_step,'ai':data_operation.data_add_id,'t':data_operation.show}
    while True:
        print('关键词有：         （网址，标题，关键词，新闻时间，新闻概述）        输入关键词时请输入这些其中之一')
        print('请输入操作（f，查找功能，s，排序功能，p，打印数据，r，返回上一操作，ai,更新或者添加id，e，退出操作,t,将操作情况打印至面板）')
        opre=input('选择什么操作')
        if opre in operation:
            data=operation[opre]()
            data_error_test=Type_error.error_dict(data)
            if data_error_test:
                pass
            else:
                continue
        else:
            print('输入格式错误，请重新输入')
            continue



