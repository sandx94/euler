import os
import random
import pdb
import math

def main():
    
    n = 1
    traingle_no = 0
    ls_facs = []
    
    while (True):
        traingle_no = n * (n+1) / 2
        ls_facs.append(traingle_no)
        fac_count = get_total_no_of_factors(traingle_no)
    
        if fac_count >= 500:
            print traingle_no
            print ls_facs
            return traingle_no

        n += 1
    print traingle_no
    print ls_facs
    print fac_count

#---
#---

def recursively_divide(num, list_of_primes):
    num_copy = num
    i = 0
    prime_factors = []
    while i < len(list_of_primes):
        if num_copy == 1:
            break
        if num_copy % list_of_primes[i] == 0:
            prime_factors.append(list_of_primes[i])
            num_copy = num_copy / list_of_primes[i]
            continue
        i += 1

    print prime_factors
    return prime_factors

#----




#----
def get_prime_factors(num):
    end = int(math.sqrt(num))
    i = 2
    all_primes = []
    while i < end:
        if is_prime(i) == True:
            all_primes.append(i)

    # verify if all_primes is [2,3,5,7] for 72
    ls_to_count = recursively_divide(num,all_primes)
    return ls_to_count
#----

def is_prime(num):
    i = 1
    count = 0
    while(i <= num):
        if num % i == 0:
            count += 1
        i += 1
    if count <= 2:
        return True
    else:
        return False

'''
def get_total_no_of_factors(num):
    ls_to_count = get_prime_factors(num)  # expected [2,2,2,3,3]
    unique_numbers = []
    powers = []
    
    for i in ls_to_count:
        if i in unique_numbers:
            continue
        unique_numbers.append(i)
        powers.append(ls_to_count.count(i))

    prod = 1
    for i in powers:
        prod = prod * (i+1)

    #pdb.set_trace()
    return prod
'''

def get_total_no_of_factors(n):
   
    number_of_factors = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            number_of_factors += 2
        else:
            continue
    return number_of_factors    

    
if __name__ == '__main__':
    #recursively_divide(72,[2,3,5,7])
    main()
    #get_total_no_of_factors(72)
    #get_prime_factors(72)
    #get_prime_factors(72)
    
    
