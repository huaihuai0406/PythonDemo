#!/usr/bin/env python
# encoding: utf-8

class Node:
    def __init__(self, parent, nodename, dist):
        self.parent = parent
        self.nodename = nodename
        self.dist = dist

    def create(self):
        self.open = []
        self.close = []
        self.path = []
        self.g = [1,2,3,4,5,]
