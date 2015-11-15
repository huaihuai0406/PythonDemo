#!/usr/bin/env python
# encoding: utf-8

import sys
import os


def readline(filename):
    f = open(filename, 'r')
    line = f.read()
    print line


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print '[-]' + filename + ' does not exit.'
            exit(0)
        if not os.access(filename, os.R_OK):
            print '[-]' + filename + ' access denied'
            exit(0)
    else:
        print '[-] Usage: ' + str(sys.argv[0]) + ' <filename>'
        exit(0)
    print '[+] Reading from: ' + filename
    readline(filename)

if __name__ == '__main__':
    main()
