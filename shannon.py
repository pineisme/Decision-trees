# _*_ coding: utf-8 _*_
"""
date: '2019/7/20 14:37'
....................................

"""
from math import log
import votee
def calcShannon(dataset):
    """
    计算信息熵
    :param dataset:
    :return: database.labels的信息熵
    """
    elemCount=len(dataset)
    labelsCount={}
    for elemvec in dataset:
        currentLabels=elemvec[-1]
        if currentLabels not in labelsCount.keys():
            labelsCount[currentLabels]=0
            labelsCount[currentLabels]+=1
    shanon=0.0
    for key in labelsCount:
        p=labelsCount[key]/elemCount
        shanon-=p*log(p,2)#以二为底
    return shanon

def splitDataset(dataset,index,value):#index是想要按照那一列特征进行分类，value是当某一行的index列为value时加入分类
    selectedData=[]
    for datavec in dataset:
        if datavec[index]==value:
            selectedVec=datavec[:index]
            selectedVec.extend(datavec[index+1:])#append =[1,2,[1,2]] extend =[1,2,1,2]#这两行的目的是去除作为index的那一列
            selectedData.append(selectedVec)
    return selectedData

def chosoeBestFeature(dataSet):
    numFeature=len(dataSet[0])-1#数据集的最后一列是标签
    baseEntropy=calcShannon(dataSet)
    bestInfoGain=0.0
    baseFeature=-1
    for i in range(numFeature):
        print('no: ',i)
        featList=[]
        for example in dataSet:
            featList.append(example[i])#注意如果要打印的话要使用list comprehension，而不是generator comprehension
        print('featlist:',featList)
        #print(type(featList))
        nuiqueFeat=set(featList)#集合没有重复元素,list is unhashable，because it will change
        newEntropy=0.0#新的熵
        print('unique feat: ',nuiqueFeat)
        for value in nuiqueFeat:
            #print('value: ',value)
            newSelectedDataBase=splitDataset(dataSet,i,value)
            #print(newSelectedDataBase)
            p=len(newSelectedDataBase)/len(dataSet)
            #print('P=%f'%p)
            newEntropy+=p*calcShannon(newSelectedDataBase)

        infoGain=baseEntropy-newEntropy#信息增益是熵的减少
        if infoGain>bestInfoGain:
            bestInfoGain=infoGain
            bestfeature=i
        print('the no%dfeature has newEntropy %f'%(i,newEntropy))
    return bestfeature
def creatTree(dataSet,labels):
    classList=[]
    for example in dataSet:
        classList.append(example[-1])
    if classList.count(classList[0])==len(classList):#.count(sub)计算sub在list中出现的次数
        return classList[0]
    if len(dataSet[0])==1:
        return  votee.majorCnt(classList)
    bestFeat=chosoeBestFeature(dataSet)
    beatFeatLabel=labels[bestFeat]
    myTree={beatFeatLabel:{}}
    del(labels[bestFeat])
    for lizi in dataSet:
        featValue=lizi[bestFeat]
    uniqueVals=set(featValue)
    for val in uniqueVals:
        sublabels=labels[:]#为了不破坏原有的所以复制一份
        myTree[beatFeatLabel][val]=creatTree(splitDataset(dataSet,bestFeat,val),sublabels)
    return myTree