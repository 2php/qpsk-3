#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 17:50:49 2018
@author: wsj

"""
#import random
#import numpy as np
#import scipy.signal as signal
#from rcos import h_rcos
#import matplotlib.pyplot as plt
import socket
import json

class Receiver(object):

    def __init__(self, M, N, f ,baud):
        self.__M = M
        self.__N = N
        self.__sps = 1e2
        self.__f = f
        self.__baud = baud
        self.__symbol = []

    def RF_launch(self):
        address = ('127.0.0.1', 31500)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(address)
        json_string, addr = s.recvfrom(20480)
        mylist = json.loads(json_string.decode('utf-8'))
        s.shutdown(socket.SHUT_RDWR)
        s.close()
        return mylist
    def get_attribute(self):
        print('M = %d' % self.__M)
        print('N = %d' % self.__N)
        print('sps = %d' % self.__sps)
        print('f = %d' % self.__f)
        print('baud = %d' % self.__baud)
        
    def _get_symbol(self):
        print('symbol = ',self.__symbol)

if __name__ == '__main__':
    my_Receive = Receiver(4,1,20e3,1e3)
    print(my_Receive.RF_launch())
#    my_Sender.get_attribute()
#    my_Sender._Sender__symbol_generator()
#    print((my_Sender._Sender__pulse_shaping()))
#    my_Sender._get_symbol()
#    fig,axes = plt.subplots(nrows=1,ncols=1,figsize=(12,18))
#    qpsk_highband = np.array(my_Sender._Sender__pulse_shaping()).T
#    print(np.shape(qpsk_highband))
#    fig,axes = plt.subplots(nrows=1,ncols=1,figsize=(12,10))
#    axes.plot(qpsk_highband)
#    fig.savefig('simulation.png',dpi=500,bbox_inches='tight')
#    plt.close()
    
    
    
    