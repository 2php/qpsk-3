#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 10:35:30 2018
@author: wsj

"""
import sender
import receiver
from multiprocessing import Pool
import os, time, random
def send(name):
#    print('Run task %d (%d)...' % (name, os.getpid()))
#    start = time.time()
    my_Sender = sender.Sender(4,1,20e3,1e3)
    my_Sender.RF_launch()
#    time.sleep(3)
#    print('send end')
#    time.sleep(1)
#    end = time.time()
#    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
def rev(name):
#    print('Run task %s (%s)...' % (name, os.getpid()))
#    start = time.time()
#    end = time.time()
    my_Receive = receiver.Receiver(4,1,20e3,1e3)
    print(my_Receive.RF_launch())
#    print('rev end')
#    time.sleep(1)
#    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(5)
    p.apply_async(rev, args=(0,))
    p.apply_async(send, args=(1,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
