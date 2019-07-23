# _*_ coding: utf-8 _*_
"""
date: '2019/7/20 14:56'
....................................

"""
def creatDatabase(path):
    dataset=[]
    with open(path,'r') as f:
        reader=f.readlines()
        linenumber=len(reader)
        for rows in reader:
            lines=rows.strip()#默认为空格
          #  lines=lines.split()
            listlines=lines.split()#通过指定分隔符对字符串进行切片
            dataset.append(listlines)
   # dataset=[[1,1,'yes'],
   #          [1,0,'yes'],
    #         [1,0,'no'],
    #         [0,1,'no'],
    #         [0,1,'no']]
    labels=['no surfacing','flipper']
    return dataset,labels

