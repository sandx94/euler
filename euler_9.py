import os
import math
import sys

def main():
    a = 1
    
    while a <= 1000:
        b = 1
        while b <= 1000:
            c = 1000 - a -b
            if c*c == (a*a + b*b):
                return a*b*c
            b += 1
        a += 1    
    
               
if __name__ == '__main__':
    x = main()    
    print x
    
            
            
