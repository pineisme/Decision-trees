import operator


def majorCnt(classsList):
    classCount = {}  # dict
    for vote in classCount:
        if vote not in classCount.keys():
            classCount[vote] = 0;
        classCount[vote] += 1
    sortedClassCount = sorted(classCount, key=lambda x: x[1], reverse=True)
    return sortedClassCount[0][1]


# _*_ coding: utf-8 _*_
"""
date: '2019/7/22 19:48'
....................................

"""