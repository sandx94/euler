import os
import itertools
import math

dc_prime = {}

def main():
    num = 3
    total_count = 0
    ls_tot = [2,5]
    while num <= 1000000:
        if circ(num):
#            
            total_count += 1             
            ls_tot.append(num)
            
        num += 2
    
    #print total_count            
    print "ls_total --> {} / len --> {}".format(ls_tot, len(ls_tot))
    
#------------------
def valid(num):
    '''
    if num % 2 == 0:
        return False
    '''    
    if num % 5 == 0:
        return False
        
    else:
        return True    
#------------------    
def circ(num):
    if not valid(num):
        return False
        
    str_num = str(num)
    i = 0
    ls_cir = []
    length = len(str_num)
    ls_cir.append(int(str_num))
    
    while i < length - 1:
        str_num = str_num[1:] + str_num[0]
        ls_cir.append(int(str_num))
        i += 1
        
    #print ls_cir
    for i in ls_cir:
        if i in dc_prime:
            val = dc_prime[i]
        else:    
            val = is_prime(i)
            dc_prime[i] = val
            
        if not val:
            return False
            
    return True
        
#------------------
def is_prime(num):
    div = 2
        
    while div <= (math.sqrt(num)):
        if num % div == 0:
            #print "False"
            return False
            
        div += 1
  
    #print "True"
    return True 
#------------------

if __name__ == '__main__':
    #circ(83)
    main()
    #is_prime(83)
    
    
