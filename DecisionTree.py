# -*- coding: utf-8 -*-  
from math import log

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featvec in dataSet:
        currentLabel = featvec[-1]
        print currentLabel
        if currentLabel not in labelCounts:
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel]+=1
    
    shannonEnt = 0.0;
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob*log(prob,2)
    return shannonEnt

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
    print calcShannonEnt(dataSet)