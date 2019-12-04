from collections import Counter
import jieba
#pip install -i http://pypi.tuna.tsinghua.edu.cn/simple  jieba
#统计参数中每个英文单词出现的次数
def stats_text_en(text,count):
    elements=text.split()
    words=[]
    symbols=',.*-!'
    for element in elements:
        for symbol in symbols:
            element=element.replace(symbol,'')
        #用str类型的isascii方法判断是否是英文单词
        if len(element) and element.isascii():
            words.append(element)
    return Counter(words).most_common(count)

#统计参数中每个中文汉字出现的次数
def stats_text_cn(text,count):
    words=jieba.cut(text)
    tmp=[]
    for i in words:
        if len(i)>1:
            tmp.append(i)
    return Counter(tmp).most_common(count)

def stats_text(text,count):
    '''
    合并英文词频和中文词频的结果
    '''
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型，输入类型%s'%type(text))
    return stats_text_cn(text,count)