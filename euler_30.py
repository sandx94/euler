import os
import math

def main():

    number = 2      
    total = []
    sums = 0
    lim = 200000 

    while number <= lim:
        string = str(number)
#                    
        ls_numbers = list(string)     

        if is_narcc(ls_numbers, number): 
            total.append(number)   
        
        number += 1

    sums = sum(total)
        
    print sums
    print total
    return sums
#----   
def is_narcc(ls_numbers, number):
    add = 0    
         
    for i in ls_numbers:
        add = add + (int(i)**5)
        if add > number:
            return False
    
    if add == number:
        return True
    else:
        return False         
           
     
#----     
if __name__ == '__main__':
    main()
    
    
    

