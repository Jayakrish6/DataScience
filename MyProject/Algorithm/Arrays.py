# -*- coding: utf-8 -*-

numbers = [10, 20, 30, 40, 50]

#numbers[1] = 'Adam'

#numbers.insert(1, 'Jack')
for num in numbers:
    print(num)
    
for i in range(len(numbers)):
    print(numbers[i])
print(numbers[:-2])

print('=====================================')
maximum = numbers[0];
        
for num in numbers:
    if num > maximum:
        maximum = num
        print('num:', num)
    elif(num < maximum):
        print('Inside elif statement')
    else:
        print('Inside last else statement')
            
        
       
print('maximum', maximum);
print('=====================================')

score_theory = 60
score_practical = 20

if(score_theory < 50):
    print("Please check the input score for 'Theory'.")
else:
    if(score_practical > 50):
        print("Please check the input score for 'Practical'.")  
    else:
        print("Score validated. Your total is: ",score_theory + score_practical)
        

print('======================================================')
coursework = "English"
score_theory = 53
score_practical = 35

if(coursework == "Science" or coursework == "science"):
    if(score_theory > 50):
        print("Please check the input score for 'Science: Theory'.")
    elif(score_practical > 50):
            print("Please check the input score for 'Science: Practical'.")  
    else:
        print("Score validated for Science. Your total is: ",score_theory + score_practical)             
elif(coursework == "English" or coursework == "english"):
    if(score_theory > 60):
        print("Please check the input score for 'English: Theory'.")
    elif(score_practical > 40):
            print("Please check the input score for 'English: Practical'.")  
    else:
        print("Score validated for English. Your total is: ",score_theory + score_practical)
else: print("Coursework not recognised. Please enter score for either Science or English.")

print('======================================================')

