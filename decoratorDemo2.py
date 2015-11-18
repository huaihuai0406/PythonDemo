#!/usr/bin/env python
# encoding: utf-8


def printB(fn):
    def wrapped():
        return "printB " + fn() + "printb "
    return wrapped


def printLi(fn):
    def wrapped():
        return "printLi " + fn() + "printli "
    return wrapped


@printB
@printLi
def hello():
    return "hello world"
print hello()

# printB printLi hello world printli printb
