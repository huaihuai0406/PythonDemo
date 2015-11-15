#!/usr/bin/env python
# encoding: utf-8


class fun2(object):

    def __init__(self):
        self.realSubList = []

    def getRealSubSet(self,fromList,toList):
        if len(fromList) <= 1:
            return
        for id in range(len(fromList)):
            arr = [i for i in fromList if i != fromList[id]]
            self.getRealSubSet(arr,toList)
            if toList.count() == 0:
                toList.append(arr)
        self.realSubList = toList
