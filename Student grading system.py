#Student grading system which displays what grade a student has based on score in a score

"""
score between 100-80 is A
score between 79-65 is B
score between 64-50 is C
score between 49-40 is D
score between 39-30 is E
score between 29-0 is F

scores cannot be more than 100 or less than 0

"""

print ("welcome to your institution's grading system \n")

score = float(input ("Kindly type your score....."))

if (score<=100 and score>79):
    print ("Your grade is A")
    
elif (score<80 and score>64):
    print ("Your grade is B")
elif (score<65 and score>49):
    print ("Your grade is C")
elif (score<50 and score>39):
    print ("Your grade is D")
elif (score<40 and score>29):
    print ("Your grade is E \nYou have a carrover in this course")
elif  (score<30 and score>=0):
    print ("Your grade is F \nYou have a carryover in this course")

else:
    print ("score is invalid")
