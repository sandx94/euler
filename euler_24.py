import os
import itertools
import math

def test(pos):                                #-- A test function only
    ls = [0,1,2,3,4,5,6,7,8,9]                  
    it =  itertools.permutations(ls,len(ls))
    count = 0

    for i in it:
        if count == pos:
            tup = i
#
            
        count += 1
    
    q = ''
    #print tup
    for i in tup:
        q = q + str(i)
    
    #print "Test   -> ",q
    return q
   
#----

def divide(pos):
    i = 0
    ls = [0,1,2,3,4,5,6,7,8,9]
    q = ''
    length = len(ls)
    
    while i < length:
        quo = pos / (math.factorial(len(ls) - 1))
        digit = ls[quo]
        q = q + str(digit)
        pos = pos % (math.factorial(len(ls) - 1))
        
        ls.remove(digit)
        
        i += 1
        
    print q
    return q
#----

    
if __name__ == '__main__':
    divide(999999)
   
    
       
