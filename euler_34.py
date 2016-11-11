import os
import itertools
import sys
import math

dc_facts = {}

#-----
def main():
    num = 3
    total = 0
    ls_fin = []
    
    for i in range(0,10):
        dc_facts[str(i)] = math.factorial(i)
    
    while num <= 2903040:
        if valid(num):
    
            string = str(num)
            add = 0           
                
            for i in string:
                add = add + dc_facts[i]    
                    
            if add == num:
                ls_fin.append(add)
        
        num += 1
    
    total = sum(ls_fin)                 
    print "Sum of curious numbers --> {}".format(total)
    return total
    
#----


def valid(num):
    
    string = str(num)

    for i in string:
        if num < dc_facts[i]:
            return False
        
    return True   
             

#----
if __name__ == '__main__':
    main()
   



