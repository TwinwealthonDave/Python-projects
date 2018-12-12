import time

print ("Welcome to the  CBT practice\nKindly register before starting your practice")

x = (input ("Enter your Full Name\n"))

print ('Please wait.......\n')
time.sleep(2)
print ("WELCOME", x)
time.sleep(2)
print ('\nThis CBT practice comprise three (3) subjects namely:\nMathematics\nEnglish Language\nGeneral Paper\n')

y = (input ("Choose subject\n"))
time.sleep(6)

if (y == 'Mathematics' or 'maths' or 'Maths'):
    print ("You have chosen Mathematics CBT PRACTICE QUESTIONS\n")

    time.sleep(6)
    print ('The test will start in 10seconds......\n')
    time.sleep(10)

    print("Question 1\nThe ages, in years, of four boys are 10,12,14, and 18. What is the average age of the boys?\nA.\t12 years\nB.\t12.5 years\nC.\t13 years\nD.\t13.5 years")
    x1 = input ('Answer = ')
    if x1 == 'D':
        print ('Correct\n\n')
    else:
        print ('Incorrect. The answer is D\nExplanation\nAverage age = sum of ages /no. of boys\nAverage age = (10+12+14+18)/4\nAverage age = 54/4 = 13.5 years\n\n')
    time.sleep (3)

    print ('Question 2\nSimplify (2√3 - 5√2)/√3\nA.\t2 - 5√2\nB.\t2 + 5√2\nC.\t2 - 5/3√6\nD.\t2 + 5/3√6')
    x2 = input ('Answer = ')
    if x2 == 'A':
        print ('Correct\n\n')
    else:
        print ('Incorrect. The answer is A\nExplanation\n(2√3 – 5√2) / √3\n(2√3 – 5√2)(√3) / √3 x √3\n((2 x 3) – 5√6) / 3\n6/3 – 5√6/3\n2 – 5√6/3\n\n')
    time.sleep (3)
    
    print ('Question 3\nExpress 0.029646 correct to three decimal places.\nA.\t0.030\nB.\t0.03\nC.\t0.029\nD.\t20.02')
    x3 = input ('Answer = ')
    if x3 == 'A' or 'a':
        print ('Correct\n\n')
    else:
        print ('Incorrect. The answer is A\nExplanation\n0.029646 correct to three decimal places\n0.029(6)  - 6 becomes 0 and approximates to 1 making 9 equal to zero and turns 2 into 3\nTherefore answer is 0.030\n\n')
    time.sleep (3)
    
    print ('Question 4\nIf y varies inversely as x and x=1/2 when y=6, find y when x=1/3.\nA.\t1/36\nB.\t9\nC.\t12\nD.\t18')
    x4 = input ('Answer = ')
    if x4 == 'B' or 'b':
        print ('Correct\n\n')
    else:
        print ('Incorrect.The answer is B\nExplanation\nIf y varies inversely as x\nThen x = k/y\n(When x = ½ and y = 6)\n1/2 = k/6 ;k = 6/2 ; k=3\n(when x = 1/3)\ny = 3/(1/3) =3 x 3 = 9\n\n')
    time.sleep (3)
    
    print ('Qustion 5\nOkon won a 200m race in 25 seconds. If he ran at the same rate, how long in minuted, would it take him to complete 800m\nA.\t2 1/2\nB.\t2\nC.\t1 2/3\nD.\t1')
    x5 = input ('Answer = ')
    if x5 == 'C' or 'c':
        print ('Correct\n\n')
    else:
        print('Incorrect. The answer is C\nExplanation\nOkon speed = 200m/25s = 8\nTo run 800m: speed = 800m/time\n8 = 800m/t(s)\nT(s) = 800m/8 = 100s\n60s = 1min\n1s = 1/60 min\n100s = (1/60) x 100 =1 2/3\n\n')
    time.sleep (3)
    
    print ("Question 6\nA piece of land was offered for N2,100,000,000.00. If the price was reduced in the ratio 3:7, find the new selling price.\nA.\tN900,000.00\nB.\tN1,100,000.00\nC.\tN1,600,000.00\nD.\tN1.800,000.00")
    x6 = input ('Answer = ')
    if x6 == 'A' or 'a':
        print ('Correct\n\n')
    else:
        print ('Incorrect. The answer is A.\nExplanation\nInitial selling price of land = N2,100,000,000\nNew price =2,100,000,000 x (3/7) = 900,000,000\n\n')
    time.sleep (3)
    
    print ('Question 7\nEvaluate: (log27/log1/3) + (log4/log√2).\nA.\t-2\nB.\t-1\nC.\t1\nD.\t7')
    x7 = input ('Answer = ')
    if (x7 == 'C'):
        print ('Correct\n\n')
    else:
        print ('Incorrect. The answer is C\nExplanation\n(log27/log1/3) + (log4/log√2)\n(3log3/-1log3) + (2log2/(1/2)log2)\n-3 +  4 = 1\n\n')
    time.sleep (3)
    
    print ('Question 8\nSolve the simultaneous equations: 3x = -y and y = x + 4.\nA.\tx = -1 and y = 3\nB.\tx = -3 and y = -1\nC.\tx = -1 and y = -3\nD.\tx = 3 and y = 1')
    x8 = input ('Answer = ')
    if x8 == 'A' or 'a':
        print ('Correct\n\n')
    else:
        print ('Incorrect. The answer is A\nExplanation\n3x = -y……………….(i)\ny = x + 4…………….(ii)\nFrom (i)  y = -3x\nsub for x in (ii)\n-3x = x + 4\n-4 = x + 3x\n-4 = 4x\nX = -1\nSub for y in (i)\ny = -3(-1)\ny = 3\nHence x = -1 and y = 3\n\n')
    time.sleep (3)
    
    print ('Question 9\nFactorize: p - bq + q - bq.\nA.\t(p - q)(1 - b)\nB.\t(p + q)(b - 1)\nC.\t(p + q)(1 - b)\nD.\t(p +q)(1 + b)')
    x9 = input ('Answer = ')
    if x9 == 'C' or 'c':
        print ('Correct\n\n')
    else:
        print ('Incorrect. The answer is C.\nExplanation\nFactorize p-bq+q-bq\np(1-b)+q(1-b)\n(p+q)(1-b)\n\n')
    time.sleep (3)
    
    print ('Question 10\nMake m the subject of the equation y=mx+c.\nA.\tm = (y - x)/c\nB.\tm = (y - c)/x\nC.\tm = x(y - c)\nD.\tm = x(y + c)')
    x10 = input ('Answer = ')
    if x10 == 'B' or 'b':
        print ('Correct\n\n')
    else:
        print ('Incorrect.The answer is B\nExplanation\ny = mx+c (making m the subject of this equation)\ny – c = mx\nm = (y - c)/x\n\n')
    time.sleep (3)


elif (y == 'English Language' or 'English' or 'english' or 'English language'):
    print ("You have chosen English Language CBT PRACTICE QUESTIONS\n")

    time.sleep(6)
    print ('The test will start in 10seconds......\n')
    time.sleep(10)

    print("Question 1\nChoose the option that best completes the sentence.\nHe did not attend the final burial .............\nA.\trite\nB.\trights\nC.\trites\nD.\tright")
    x1 = input ('Answer = ')
    if x1 == 'C' or 'c':
        print ('Correct\n\n')
    else:
        print ('Incorrect. The answer is C\nHe did not attentd the final burial RITES\n\n')
    time.sleep (3)

    print ('Question 2\nSelect the wrongly spelt word\nA.\tOccurrence\nB.\tsurprise\nC.\tpersonnel\nD.\tposses')
    x2 = input ('Answer = ')
    if x2 == 'D' or 'd':
        print ('Correct\n\n')
    else:
        print ('Incorrect. The answer is D\nPosses is spelt POSSESS\n\n')
    time.sleep (3)
    
    print ('Question 3\nI have the .......... of meeting him.\nA.\tprevilege\nB.\tprivilege\nC.\tpreviledge\nD.\tpriviledge')
    x3 = input ('Answer = ')
    if x3 == 'B' or 'b':
        print ('Correct\n\n')
    else:
        print ('Incorrect. The answer is B\nI have the PRIVILEGE of meeting him\n\n')
    time.sleep (3)
    print ('From the words lettered A to D, choose the word\nthat has the same vowel sound as the vowels in the word provided\n\n')
    print ('Question 4\nSeatA.\thide\nB.\tpeasant\nC.\thead\nD.\tpeople')
    x4 = input ('Answer = ')
    if x4 == 'D' or 'd':
        print ('Correct\n\n')
    else:
        print ('Incorrect.The answer is D\n/Si:t/ - Pi:ple/\n\n')
    time.sleep (3)
    
    print ("Qustion 5\nPass\nA.\tEarth\nB.\tClerk\nC.\tPass\nD.\tMan")
    x5 = input ('Answer = ')
    if x5 == 'C' or 'c':
        print ('Correct\n\n')
    else:
        print('Incorrect. The answer is C\n/pa:ss/ - /pa:ss/\n\n')
    time.sleep (3)

    print ('Question 6\nPower\nA.\tFlour\nB.\tHigher\nC.\tLiar\nD.\tFlier')
    x6 = input ('Answer = ')
    if x6 == 'A' or 'a':
        print ('Correct\n\n')
    else:
        print ('Incorrect. The answer is A\n/Paʊə/ - /flaʊə/\n\n')
    time.sleep (3)

    print ('Choose the option that best fills the gap.\n\n')
    print ("Question 7\nThe choice to go is ...........\nA.\tyours'\nB.\tyour\nC.\tyours\nD.\tyour's")
    x7 = input ('Answer = ')
    if x7 == 'C' or 'c':
        print ('Correct\n\n')
    else:
        print ('Incorrect. The answer is C.\nThe choice to go is YOURS\n\n')
    time.sleep (3)
    
    print ('Question 8\nMrs Godwin ............ in this school since 2001\nA.\ttaught\nB.\twas teaching\nC.\tteaches\nD.\thas been teaching')
    x8 = input ('Answer = ')
    if (x8 == 'D' or 'd'):
        print ('Correct\n\n')
    else:
        print ('Incorrect. The answer is D\nMrs Godwin HAS BEEN TEACHING in this school since 2001\n\n')
    time.sleep (3)
    print ('From the words lettered A to D,choose the word that ryhmes with the given word.\n\n')    
    print ('Question 9\nFret\nA.\tFreight\nB.\tHeight\nC.\tThreat\nD.\tThread')
    x9 = input ('Answer = ')
    if x9 == 'C' or 'c':
        print ('Correct\n\n')
    else:
        print ('Incorrect. The answer is C.\n/Frɛt/ - /Thrɛt/\n\n')
    time.sleep (3)
    
    print ('Question 10\nBreeze\nA.\tStress\nB.\tChess\nC.\tFree\nD.\tTrees')
    x10 = input ('Answer = ')
    if x10 == 'D' or 'd':
        print ('Correct\n\n')
    else:
        print ('Incorrect.The answer is D\n/Bri:z/ - /Tri:z/\n\n')
    time.sleep (3)

#elif y == General Paper or General paper:

else:
    print ('subject not available')
print ('You have completed your test.\nTo try more questions click on https://edungr.com/download-jamb-past-questions-answers-pdf-free/ to download more questions for further practice.')
