# _*_ coding: utf-8 _*_
"""
date: '2019/7/20 14:54'
....................................

"""
#ctrl+]可以跳出右括号
#检查数据集中的左右标签是否都属于同一类
#如果是则返回该类标签，如果不是则选择划分数据集最好的特征进行划分
#递归创建分支节点
import shannon
import dataBase
import votee
if __name__ == '__main__':#打出main就会出现这一句
    dataset,labels=dataBase.creatDatabase('data.txt')
    #dataset[0][-1]='maybe'
    print('dataset:',dataset)
    eShannon=shannon.calcShannon(dataset)
    print('shannon:%f'%eShannon)#熵越高混合的数据越多，熵越大越无序，按照最大信息增益进行划分
    selectedData=shannon.splitDataset(dataset,0,'1.5')
    print('selected data:',selectedData)
    print('best feature is : ',shannon.chosoeBestFeature(dataset))
    mytree=shannon.creatTree(dataset,labels)
    print(mytree)
