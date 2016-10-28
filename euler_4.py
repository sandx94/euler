import os
import sys

def rev(str1):             #-- Taking a string as a parameter
    
    str_r = ''
    for i in str1:
        str_r = i + str_r
    
    c = int(str_r)    
    return c
    
#--

def palin():
    a = 999
    #b = 9
    ls = []
    
    while(a >= 0):
    
        b = 999
        while(b >= 0):
            prod = a * b
            char = str(prod)
                     
            if(char == char[::-1]):
                real = int(char)
                ls.append(real)
                
            b -= 1
        a -= 1
         
    largest = max(ls)
     
    print "List --> ",ls 
    print "\n"
    print "Largest palindrome --> %d" % (largest)
    
#--

def num():

    num = 1000000
    i = 1
    ls = []
    
    while(num >= 0):
        fact(num)
                                 
        num -= 1
    print ls    
                
#--

def fact(num):
                          
    i = num/2
    ls = []
    while(i > 0):
        if(num % i == 0):
            if i >= 100 and (num/i) >= 100:
                lst = [i,(num/i)]
                return lst
                
            
        i -= 1
   
#--

def numb():
       
   num = 20000
   collect = []
   while(num > 0):
       
       a = is_pal(num)
       
       if a == 'True':
            fac = fact(num)
          
            collect.append(num)
            max_ans = max(collect)
            lst = fact(num) 
            
            
            #if 2 factors are 3-digit numbers,
            
             
       '''      
                ans = num
                break
    return num
       '''
       num -= 1   
   print num
   

#--

def is_pal(num):
    char = str(num)
           
    if(char == char[::-1]):
        a = "True"
          
    else: 
        a = "False"
          
    return a    
    





    
    
if __name__ == '__main__':
    palin()      
             

