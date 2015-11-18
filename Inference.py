#!/usr/bin/env python
# encoding: utf-8


import re


class Infernce:

    def __init__(self):
        self.list = []
        self.list.append(u"∀x((┐Poor(x)∧Smart(x))->happy(x))")
        self.list.append(u"∀x(Read(x)->Smart(x))")
        self.list.append(u"Read(LiMing)∧┐Poor(LiMing)")
        self.list.append(u"happy(x)->Exciting(x)")
        self.list.append(u"┐Exciting(LiMing)")

    def removalImplication(self):
        index = -314
        for ind, expr in enumerate(self.list):
            index = expr.find("->")
            if index != -1:
                if index == 0:
                    print "error"
                    return
                if expr[index - 1] == ')' and expr[index - 2] == ')':
                    sign = 1
                    point = index -2
                    while sign != 0 and point >=0:
                        if expr[point] == ')':
                            sign += 1
                        elif expr[point] == '(':
                            sign -= 1
                        point -= 1
                    if point < 0:
                        print "error"
                    else:
                        list = '' + expr[0: point + 1] + u'┐' +\
                               expr[point + 1: index] + u'∨' +\
                               expr[index + 2:]
                else:
                    point = index - 4
                    while point >= 0:
                        if expr[point] == '(':
                            break
                        point -= 1
                        list = '' + expr[0: point + 1] + u'┐' +\
                               expr[point + 1: index] + u'∨' +\
                               expr[index + 2:]
                self.list[ind] = list

    def removalOfTheUniversalWord(self):
        for ind, expr in enumerate(self.list):
            index = expr.find(u'∀')
            if index != -1:
                if index == 0 and expr[2] == '(' and expr[len(expr) - 1] == ')':
                    list = expr[3: len(expr) -1]
                    #  print list.encode('utf8')
                    self.list[ind] = list

    def removeNonSymbol(self):
        for ind, expr in enumerate(self.list):
            index = expr.find(u'┐(')
            if index != -1:
                point1 = index + 2
                point2 = index + 2
                sign = 1
                list = u'┐'
                while sign != 0:
                    if expr[point1] == '(':
                        sign += 1
                    elif expr[point1] == ')':
                        sign -= 1
                    else:
                        if expr[point1] == u'∧':
                            list += expr[point2: point1] + u'∨┐'
                            point2 = point1 + 1
                    point1 += 1
                list += expr[point2: point1 - 1]
                #  print list.encode('utf8')
                list += expr[point1:]
                self.list[ind] = list
                #  print list.encode('utf8')

        for ind, expr in enumerate(self.list):
            index = expr.find(u'┐┐')
            if index != -1:
                list = expr.replace(u'┐┐', '')
                #  print list.encode('utf8')
                self.list[ind] = list

    def resolution(self):
        list = ''
        stack = []
        for ind, expr in enumerate(self.list):
            if expr.count(u'∨') and not expr.count(u'∧'):
                list += expr + u'∨'
                print str(ind + 1) + ' ',
                stack.append(ind)
        list = list[:-1]
        if (u'∨Poor(x)' in list) and (u'┐Poor(x)' in list):
            list = list.replace(u'∨Poor(x)', '')
            list = list.replace(u'∨┐Poor(x)', '')
        if (u'∨Smart(x)' in list) and (u'┐Smart(x)' in list):
            list = list.replace(u'∨Smart(x)', '')
            list = list.replace(u'∨┐Smart(x)', '')
        if (u'∨happy(x)' in list) and (u'┐happy(x)' in list):
            list = list.replace(u'∨happy(x)', '')
            list = list.replace(u'∨┐happy(x)', '')
        while len(stack) > 0:
            del self.list[stack.pop()]
        print '归结成>>>'
        print list.encode('utf8')
        self.list.append(list)
        for s in self.list:
            print s.encode('utf8')
        for ind, expr in enumerate(self.list):
            self.list[ind] = expr.replace('(x)', '(LiMing)')
        print '替换x为LiMing'
        for s in self.list:
            print s.encode('utf8')
        sign = {0:-1, 1:-1, 2:-1}
        for ind, expr in enumerate(self.list):
            if u'∨' not in expr:
                if u'┐Read' in expr:
                    sign[0] = 0
                elif 'Read' in expr:
                    sign[0] = 1
                if u'┐Poor' in expr:
                    sign[1] = 0
                elif 'Poor' in expr:
                    sign[1] = 1
                if u'┐Exciting' in expr:
                    sign[2] = 0
                elif 'Exciting' in expr:
                    sign[2] = 1
        for ind, list in enumerate(self.list):
            if u'∧' not in list:
                if sign[0] == 1:
                    list = list.replace(u'┐Read(LiMing)', '')
                else:
                    list = list.replace('Read(LiMing)', '')
                if sign[1] == 1:
                    list = list.replace(u'┐Poor(LiMing)', '')
                else:
                    list = list.replace('Poor(LiMing)', '')
                if sign[2] == 1:
                    list = list.replace(u'┐Exciting(LiMing)', '')
                else:
                    list = list.replace('Exciting(LiMing)', '')
                regex = re.compile(u'∨+')
                list = regex.sub('',list)
                if list =='':
                    print '产生空串！'

if __name__ == "__main__":
    test = Infernce()
    test.removalImplication()
    test.removalOfTheUniversalWord()
    test.removeNonSymbol()
    test.resolution()
