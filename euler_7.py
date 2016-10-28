import os
import time
import sys
import math

def is_prime(num):
    i = 2
    str_num = str(num)
    if str_num[-1] in ('5'):

        return False
      
    while i <= math.sqrt(num):
        if num % i == 0:
# 
            return False
        i += 1       
    return True
        
#--

def main(max_prime_count_str):
    max_prime_count = int(max_prime_count_str)
    dig = 7
    no_of_prime = 3
    
    while(no_of_prime <= max_prime_count):
        
        if is_prime(dig):
            
            no_of_prime += 1
            
            if no_of_prime == max_prime_count:
                print dig
                return dig
        
        dig += 2
        
    print dig


if __name__ == '__main__':
    main(sys.argv[1])
    
