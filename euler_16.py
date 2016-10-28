import os
import math

def main():
    num = 2**1000
    
    char = str(num)
    ls = list(char)
    sums = 0
    
    for i in ls:
        sums = sums + int(i)
        
    print sums
    return sums
    
#---

if __name__ == '__main__':
    main()
