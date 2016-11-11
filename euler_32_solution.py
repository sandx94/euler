import os
import math
import sys
import pdb

def main():             
    a = 1
    prod = 0
    ls_prod = []
    ls_all = []
    limit = 999
    total = 0
    
    
    while a <= limit:
        b = a
        
        while b <= limit:
        
            if pandig(a,b):
                prod = a * b
                ls_all.append(prod)
             
                
            b += 1    
        a += 1
    
    #----------------------
 
    prod = 0
    ls_late = []
    ls_tupps = []
    
    ls_ints = calc_a()
    
    for c in ls_ints:
        b = 1
        while b <= 9:
               
            if pandig(c,b):
                prod = c * b
                print "{} * {} --> {}".format(c,b,prod)
                ls_late.append(prod)    
            
            b += 1
            
    ls_all = set(ls_all)  
    ls_all = list(ls_all)      
    
    ls_all.extend(ls_late)
    total = sum(ls_all)        
    
    print "\nSolution --> ",total
    print ls_all
    
#----  
def calc_a():
    import itertools
    x = itertools.permutations(['1','2','3','4','5','6','7','8','9'], 4)
    ls_ints = []
          
    for i in x:
        num = ''
        
        for j in i:
            num = num + str(j)
        ls_ints.append(int(num))
    
    print ls_ints
    print len(ls_ints)
    return ls_ints
  
#----

def pandig(a,b):
    
    str_a = str(a)
    str_b = str(b)
    
    len_a = len(str_a)
    len_b = len(str_b)
    
    if '0' in str_a or '0' in str_b:
        return False
    
    if len_a != len(set(str_a)):
        return False
     
    if len_b != len(set(str_b)):
        return False 
    
    prod = a * b
    
    str_prod = str(prod)
    
    if '0' in str_prod:
        return False
    
    str_total = str_a + str_b + str_prod
    ls_prods = []
    
    
    if len(str_total) != 9:
        return False
    
    set_total = set(str_total)   
    if len(set_total) != 9:
        return False
    
    return True

    return ls_prods

#----

if __name__ == '__main__':
    #calc_a()
    main()


