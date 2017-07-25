import jieba.analyse

path = '精绝古城.txt'

fp = open(path,'r',encoding='utf-8')
content = fp.read()
try:
    # jieba.analyse.set_stop_words('停用词表路径')
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
    for item in tags:
        print(item[0]+'\t'+str(int(item[1]*1000)))

finally:
    fp.close()