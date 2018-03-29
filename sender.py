#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 14:00:30 2018
@author: wsj

"""
import random
import numpy as np
import scipy.signal as signal
from rcos import h_rcos
#import matplotlib.pyplot as plt
import socket
import json
class Sender(object):

    def __init__(self, M, N, f ,baud):
        self.__M = M
        self.__N = N
        self.__sps = 1e2
        self.__f = f
        self.__baud = baud
        self.__symbol = []
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
        
    def __pulse_shaping(self):
        self.__symbol_generator()
        Fs = self.__sps*self.__baud
        upsample_mat = np.zeros((1,int(self.__sps)))
        upsample_mat[0,0] = 1
        symbol = np.transpose(np.mat(self.__symbol))
        upsample_signal = np.reshape(symbol*upsample_mat,(int(self.__sps*self.__N),1))
        qpsk_baseband = signal.convolve(upsample_signal,np.mat(h_rcos).T)
        cos_high = [np.cos(2*np.pi*self.__f*t) for t in np.arange(0,np.size(qpsk_baseband)/Fs,1/Fs)]
        sin_high = [np.sin(2*np.pi*self.__f*t) for t in np.arange(0,np.size(qpsk_baseband)/Fs,1/Fs)]
        qpsk_highband = np.multiply(np.real(qpsk_baseband).T,cos_high) + np.multiply(np.imag(qpsk_baseband).T,sin_high)
        return qpsk_highband
    def RF_launch(self):
        qpsk_highband = self.__pulse_shaping()
        print(qpsk_highband)
#        qpsk_highband = [1,2,3,4,5]
        address = ('127.0.0.1', 31500)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        json_string = json.dumps(qpsk_highband.tolist())
        s.sendto(json_string.encode('utf-8'), address)
        s.shutdown(socket.SHUT_RDWR)
        s.close()
    def get_attribute(self):
        print('M = %d' % self.__M)
        print('N = %d' % self.__N)
        print('sps = %d' % self.__sps)
        print('f = %d' % self.__f)
        print('baud = %d' % self.__baud)
        
    def _get_symbol(self):
        print('symbol = ',self.__symbol)

if __name__ == '__main__':
    my_Sender = Sender(4,1,20e3,1e3)
    my_Sender.RF_launch()
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
    
    
    
    