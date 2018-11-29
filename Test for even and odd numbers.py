# this program tells odd and even numbers when inputted by the user

print("This program tells you if the first number you provide is even or \nodd provided it is greater than the latter")

x,y = eval(input ("What are your numbers........"))

if (x > y):

          print ("x is greater than y")

          if (x % 2 == 0):

                          print ("x is also an even number")

          else:

              print ("But x is not an even number \nx is an odd number")

else:

    print ("x is less than y")
