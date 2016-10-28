import os
import time
import sys
            
#--1--

def get_min(ls):
    
    small = ls[0]
    
    for i in ls:
        if i != 1:
            if small == 1:
                small = i
            if i < small:
                small = i
                
    return small
    
#--2--

def div_by(ls, small):
    
    cd = []
    for i in ls:
        if i ==1:
            cd.append(i)
            
        elif i == small:
            cd.append(1)
            
        elif i % small == 0:
            cd.append(i/small)
            
        else:
            cd.append(i)    
    
    return cd
    
#--3--
    
def all_ones(ls):
    leen = len(ls)
    count = 0
    
    for i in ls:
        if i == 1:
            count += 1
            
    if count == leen:
        return True
        
    else:
        return False
    
#--4--    
    
def calc_prod(list_fact):
    
    fact = 1
    for i in list_fact:
        fact = fact * i
    
    return fact
 
#---main---   

def lcms(ls):
   
    list_fact = []
 
    while(not all_ones(ls)):
    
        small = get_min(ls)
        ls = div_by(ls,small)
        list_fact.append(small)    
    
    fact = calc_prod(list_fact)
    return fact
   
    
           
if __name__ == '__main__':
    ls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    lcms(ls)
    
