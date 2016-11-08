#-- Project euler problem 23

import os
import math
import sys

def main():
    i = 1
    lim = 28123
    ab_nos = []
    add = 0
    total_sum = 0   
#    
    while i <= lim:
        if is_abun(i):
            ab_nos.append(i)
                       
        i += 1    
    dc_sums = {}
    ls_sums = []
    count_comb = 0
    
    x = 0
    while x < len(ab_nos):
        if ab_nos[x] > (lim / 2):
            break
        y = x
        while y < len(ab_nos):
            c = ab_nos[x] + ab_nos[y]
            count_comb += 1
            if c > lim:   
                break
            
            if c not in dc_sums:
                dc_sums[c] = 1
            
            y += 1
        x += 1    
    print "combinations --> ",count_comb
    i = 1
    while i < lim:
        if i not in dc_sums:
            total_sum = total_sum + i    
        
        i += 1
    print total_sum
    return total_sum
        
#----
def is_expresible(num,comb_ab):
    for i in comb_ab:
        if num > comb_ab[0]:
            return True
            #break
             
        else:
            return False     


#----
def is_abun(num):
    flag = True
    ls_facs = calc_facs(num)
    
    sums = 0
    for j in ls_facs:
        sums = sums + j
    
    
    if sums > num: 
        return True
    
    else:
        return False
        
#----
def calc_facs(num):
    
    ls_facs = [1]
    i = 2
        
    while i <= math.sqrt(num):
        if num % i == 0:
            ls_facs.append(i)
                
            if i != (num/i):
                ls_facs.append(num/i)
            
            ls_facs.sort()
            
        i += 1
         
    return ls_facs
 
 
#----

if __name__ == '__main__':
    
    main()
