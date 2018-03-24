#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 14:00:30 2018
@author: wsj

"""
import random
#import math

class Sender(object):

    def __init__(self, M, N, sps, f ,baud):
        self.__M = M
        self.__N = N
        self.__sps = sps
        self.__f = f
        self.__baud = baud

    def __symbol_generator(self):
        self.__symbol = [random.randrange(self.__M) for i in range(self.__N)]
        if self.__M == 2:
            map_dict = {0 : -1,1 : 1}
        elif self.__M == 4:
            map_dict = {0 : -1+1j, 1:-1-1j, 2:1+1j, 3:1-1j}
        else:  
            raise Exception('M is wrong,it is only 2 or 4')
            
        def int2complex(i):
            return map_dict[i]
        self.__symbol = list(map(int2complex,self.__symbol))
        
 
    def get_attribute(self):
        print('M = %d' % self.__M)
        print('N = %d' % self.__N)
        print('sps = %d' % self.__sps)
        print('f = %d' % self.__f)
        print('baud = %d' % self.__baud)
        
    def get_symbol(self):
        print('symbol = ',self.__symbol)

if __name__ == '__main__':
    my_Sender = Sender(4,10,1e2,20e3,1e3)
    my_Sender.get_attribute()
    my_Sender._Sender__symbol_generator()
    my_Sender.get_symbol()
    
    
    
    