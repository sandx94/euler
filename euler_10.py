import os
import math
import sys
import time

def main(limit):

    num = 3
    sum_primes = 7
              
    ls_prime = []
           
#
    while num <= limit:
        
        if is_prime(num, ls_prime):
            ls_prime.append(num)
            sum_primes = sum_primes + num
            
        num += 2
        
    print sum_primes
    ls_prime.extend([2,5])
    ls_prime.sort()
    #print ls_prime
    
          
#---------------------------

def is_prime(num, ls_prime):  #-- Methodto check ifprime or not
    
    str_num = str(num)
    if str_num[-1] in ('5'):
        return False
    
    sq_num = math.sqrt(num)
    for i in ls_prime:
        if i > sq_num:
            break
        if num % i == 0:
            return False
    return True
    
#---------------------------
         
if __name__ == '__main__':
    main(2000000)
    
