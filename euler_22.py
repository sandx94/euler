import os
import random
import sys
import math

dc_val = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}


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
        val = val + dc_val[i]
        
    
    val = val * pos
    
    print "name = {} / val = {}".format(name,val)
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
    
