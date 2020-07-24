#!/usr/bin/env python

import sys
args=list(sys.argv)
board_args=['b9','b11','h','l']

#Takin'Args

for i in args[1::]:
    if i in board_args:
        if i[0]=='b':
            size=i[1:]
            break
        if i=='h':
            print('help')
            break
        if i=='l':
            print('load')
            break
    elif not args[1]:
        print('menu')

    else:
        print('non-valid arg')

