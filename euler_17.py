import os
import time
import sys

def word():
    n = 674
        
    count = 0    
        
    if (n < 1) or (n > 1000):
        print "\nERROR.. !! Invalid number !\n"         
    
    
    else:         
            
        
        dc_unit_a = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine',10:'Ten', 0:'', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}
            
            #--
            
            #dc_unit_b = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 0:''}
            
            #--
            
        dc_tens = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety', 0:''}
        
        
         
            #--
               
        check = n % 100
            
        if(check <= 19):   
            
            a = n % 100
            n = n/100
                
            b = n                           
               
            str_1 = dc_unit_a[b] +' hundred and '+ dc_unit_a[a]
                   
            #--
            
        elif(check > 19):
                
            a = n % 10                   
            n = n/10
                
            b = n % 10                      
            n = n/10
                
            c = n                         
               
            str_1 = dc_unit_a[c] + ' hundred and ' + dc_tens[b] +' '+ dc_unit_a[a]
                
        #--                         
   
    print str_1

#---

if __name__ == '__main__':
    word()        

        
