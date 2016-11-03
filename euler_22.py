import os
import random
import sys
import math

#------
def read_file():
    fob = open("euler_22.txt", "r")
    y = fob.read()

    y1 = y.replace('"', '')
    y2 = y1.strip()
    
    ls_names = y2.split(",")
    ls_names.sort()
    
    value = calc_val(ls_names)
    
    print value
#------                 
def word_cnt(name, pos):
    val = 0
        
    for i in name:
        val = val + (ord(i) - 64)
        #print i
    val = val * pos
    
    print "name = {}".format(name)
    return val
    
#-----    
def calc_val(ls_names):
    count = 1
    rank = 0   
       
    for name in ls_names:
        rank = rank +  word_cnt(name, count)        
        count += 1
    
    return rank
        
               
if __name__ == '__main__':
    read_file()    
    
