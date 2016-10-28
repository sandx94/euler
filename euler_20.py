import os
import math

def main():

    x = str(math.factorial(100))
    
    add = 0
    for i in x:
        add = add + int(i)
        
    print add
    
if __name__ == '__main__':
    main()
