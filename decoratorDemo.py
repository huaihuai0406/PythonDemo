#!/usr/bin/env python
# encoding: utf-8

import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print 'begin %s %s():' % (text, func.__name__)
            fun = func(*args, **kw)
            print 'end %s %s():' % (text, func.__name__)
            return fun
        return wrapper
    return decorator


@log('call')
def now():
    print '2015-11-17'

now()
