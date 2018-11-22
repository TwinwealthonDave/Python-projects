#To solve the quadratic equation ax**2+bx+c=0

import math

#For the user to input his values

a = float (input ("what is the value of a?  "))
b = float (input ("what is the value of b?  "))
c = float (input ("what is the value of c?  "))

#declare discriminant

d = (b**2) - (4*a*c)

x1 = (-b + math.sqrt (d))/2*a
x2 = (-b - math.sqrt (d))/2*a 

print ("The solutions (x1 and x2) of the quadratic equations are shown below")

print (x1)

print (x2)

