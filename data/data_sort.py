#coding:utf-8
import time
import pypinyin



def data_test(f):
    def test(data,keyword,reverse):
        try:
            len(data)
        except:
            return -6
        else:
            datas=data.copy()
            return f(datas,keyword,reverse)
        finally:
            del datas
    return test
def __not_vally(data,keyword):
    try:
        data[0][keyword]
    except :
        print('关键字输入错误，获取的信息信息中没有该关键字哦！')
        return True


def __compear_data(data,keyword='新闻时间'):
        if keyword == '新闻时间':
            try:
                data_time=time.strptime(data,'%Y-%m-%d %H:%M:%S')
            except:
                print('数据错误')
                exit(-3)
            else:
                return int(time.mktime(data_time))
        elif keyword == 'id':
            return int(data)
        else:
            if data == '':
                return ''
            else:
                return pypinyin.lazy_pinyin(data[0])[0]


def __heaps(data,keyword,reverse):
    def __heap(node_index, data, keyword, reverse):
        if node_index != 0:
            if reverse:
                if __compear_data(data[node_index][keyword], keyword) > __compear_data(data[(node_index - 1) // 2][keyword], keyword):
                    data[node_index], data[(node_index - 1) // 2] = data[(node_index - 1) // 2], data[node_index]
                    __heap((node_index - 1) // 2, data, keyword, reverse)
            else:
                if __compear_data(data[node_index][keyword], keyword) < __compear_data(data[(node_index - 1) // 2][keyword], keyword):
                    data[node_index], data[(node_index - 1) // 2] = data[(node_index - 1) // 2], data[node_index]
                    __heap((node_index - 1) // 2, data, keyword, reverse)
    for node_index in range(1, len(data)):
        __heap(node_index,data,keyword,reverse)

@data_test
def bubble_sort(data,keyword='新闻时间',reverse=False):
    '''

    :param data: [{}]类型的数据
    :param keyword: 查询关键词
    :param reverse: 正序还是逆序，false正序，true，逆序
    :return: 排序好的[{}]类型
    '''
    if __not_vally(data,keyword):
        return -1
    for big_carrent in range(len(data)-1):
        flug=0
        for small_carrent in range(len(data)-1):
            if  reverse:
                if __compear_data(data[small_carrent][keyword],keyword) < __compear_data(data[small_carrent+1][keyword],keyword):
                    flug = 1
                    data[small_carrent], data[small_carrent + 1] = data[small_carrent + 1], data[small_carrent]
            else:
                if __compear_data(data[small_carrent][keyword],keyword) > __compear_data(data[small_carrent+1][keyword],keyword):
                    flug=1
                    data[small_carrent],data[small_carrent+1]=data[small_carrent+1],data[small_carrent]
        if flug==0:
            return data
    return data

@data_test
def heap_sort(data,keyword='新闻时间',reverse=False):
    '''

    :param data: [{}]类型的数据
    :param keyword: 查询关键词
    :param reverse: 正序还是逆序，false正序，true，逆序
    :return: 排序好的[{}]类型
    '''
    if __not_vally(data,keyword):
        return -1

    def heap_out():
        datas=data.copy()
        sort_data=[]
        while datas:
            __heaps(datas,keyword,reverse)
            sort_data.append(datas.pop(0))
        return sort_data
    return heap_out()




def partial_sort(data,topn,keyword='新闻时间',reverse=False):
    '''
    :param data: [{}]类型的数据
    :param keyword: 查询关键词
    :param reverse: 正序还是逆序，false正序，true，逆序
    :return: 排序好的[{}]类型
    :param topn: 希望获得前几的数据:int
    '''
    try:
        len(data)
    except:
        return -6
    reverse=not reverse
    if __not_vally(data,keyword):
        return -1
    if topn > len(data):
        return -2
    sort_data=data[:topn]
    choice_data=data[topn:]
    __heaps(sort_data,keyword,reverse)
    for choice_node in choice_data:
        if reverse:
            if __compear_data(choice_node[keyword],keyword) < __compear_data(sort_data[0][keyword],keyword):
                sort_data[0]=choice_node
                __heaps(sort_data, keyword, reverse)
        else:
            if __compear_data(choice_node[keyword],keyword) > __compear_data(sort_data[0][keyword],keyword):
                sort_data[0]=choice_node
                __heaps(sort_data, keyword, reverse)
    reverse = not reverse
    return heap_sort(sort_data,keyword,reverse)



@data_test
def magic_sort(data,keyword='新闻时间',reverse=False):
    '''

    :param data: [{}]类型的数据
    :param keyword: 查询关键词
    :param reverse: 正序还是逆序，false正序，true，逆序
    :return: 排序好的[{}]类型
    '''
    keyword=keyword.split('，')
    for k in keyword:
        if __not_vally(data,k):
            return -1
    data=sorted(data,key=lambda x:tuple(map(lambda y: x[y], keyword)),reverse=reverse)
    return data


