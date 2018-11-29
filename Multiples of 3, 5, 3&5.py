"""
this program counts from 1 to 100
It substitutes multiples of 3 with fizz,
multiples of 5 with buzz
and multiples of 3&5 with fizzbuzz

"""

x = 1

while(x <= 100):
    
        if((x % 5 == 0) and (x % 3 == 0)):
                print('fizzbuzz')
                
        elif(x % 5 == 0):
                print('buzz')
                
        elif(x % 2 == 0):
                print('fizz')
                
        else:                 
                print(x)
        x += 1  
