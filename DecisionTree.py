# -*- coding: utf-8 -*-  
from math import log

#计算信息熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    #for循环将所有的特征个数统计出来，放到labelCounts里面
    for featvec in dataSet:
        currentLabel = featvec[-1]
        print currentLabel
        if currentLabel not in labelCounts:
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel]+=1
    #遍历labelCounts,计算信息熵
    shannonEnt = 0.0;
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob*log(prob,2)
    return shannonEnt

#划分数据集
def splitDataSet(dataSet,axis,value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            #将axis这一个特征去掉
            reducedFeatVec = featVec[:axis] 
            reducedFeatVec.extend(featVec[axis+1:])
            #拼装起来
            retDataSet.append(reducedFeatVec)
    return retDataSet

#选择最好特征来进行划分
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet) #计算总的信息熵
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def createDataSet():
    dataSet=[[1,1,'yes'],
             [1,1,'yes'],
             [1,0,'no'],
             [0,1,'no'],
             [0,1,'no']]
    labels = {'no surfacing','flippers'}
    return dataSet,labels

if __name__ == "__main__":
    dataSet,labels = createDataSet();
    print splitDataSet(dataSet,0,1);
