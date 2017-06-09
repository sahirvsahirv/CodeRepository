#Example 1
#I am a comment

#Variable
summation = 0
print(summation)
#I print an empty line
print("\n")

#Result 1 - Expected output below ( without #)
#0

#-------------------------------------------------

#Example 2

#Add 10 to the variable
summation = summation + 10
print("sum = {}".format(summation))

print("\n")

#Result 2 - Expected output below ( without #)
#sum = 10
#-------------------------------------------------

#Example 3

#for loop
summation = 0
for counter in range(5):
    summation=summation+counter
    print("sum = {}".format(summation))

#Result 3 - Expected output below ( without #)
##sum = 0
##sum = 1
##sum = 3
##sum = 6
##sum = 10

print("I am outside the for loop and I will print only once")
print("sum = {}".format(summation))

print("\n")

#Result 3 - Expected output below ( without #)
##I am outside the for loop and I will print only once
##sum = 10
#-------------------------------------------------
#Example 4

#for loop with range and a step and if conditions
#0 - the loop starts from 0
#10 - the loop stops
#2 - skip 2
for i in range(0, 10, 2):
    #another way to print
    print("counter =", i)
print("\n")  
#Result 4 - Expected output below ( without #)
##counter = 0
##counter = 2
##counter = 4
##counter = 6
##counter = 8
#-------------------------------------------------

#Example 5
#Above problem with an if condition

for i in range(10):
    #another way to print
    if(i%2 == 0): #if divisible by 2
        print("counter =", i)
print("\n")
#Result 5 - Expected output below ( without #)
##counter = 0
##counter = 2
##counter = 4
##counter = 6
##counter = 8
#-------------------------------------------------
#Example 6
#Another method - for loop - take input
summation = 0
maxnum =  input("Enter the num till want to calculate natural numbers - ")
#maxum is a string, since input function receives everything as a string
for counter in range(int(maxnum)):
    summation=summation+counter
    print("sum = {}".format(summation))

print("I am outside the for loop and I will print only once")
print("sum = {}".format(summation))

print("\n")
#Result 6 - Expected output below ( without #)

##Enter the num till want to calculate natural numbers - 3
##sum = 0
##sum = 1
##sum = 3
##I am outside the for loop and I will print only once
##sum = 3
#-------------------------------------------------
#Example 6
#Add the values recived in a list and print all outside the for loop
summation = 0
#Initialize an empty list to store all the incremental sums
sumlist = []
for counter in range(5):
    summation=summation+counter
    sumlist.append(summation)

print("\n")
print("I am outside the for loop and I will print only once")
print("all the collected incremental sums = {}".format(sumlist))

print("\n")

#Result 6 - Expected output below ( without #)

##I am outside the for loop and I will print only once
##all the collected incremental sums = [0, 1, 3, 6, 10]

#-------------------------------------------------
#Example 7

#nested loops example
#accept marks for students and print
students = []
subjectmarks = []

#Since you don't know how much to loop, ask and receive input from the user
numstudents = input("Enter the number of students - ")
numsubjects = input("Enter the number of subjects - ")

#Receive input and store the marks against each student
for stu in range(int(numstudents)):
    name = input("Enter student name - ")
    for marks in range(int(numsubjects)):
        marks = input("Enter each subject marks - ")
        students.append([name, marks])
        
for stu in students:
    print("Student name = {} and marks = {}".format(stu[0],stu[1]))
print("\n")

#Result 7 - Expected output below ( without #)

##Enter the number of students - 2
##Enter the number of subjects - 2
##Enter student name - Gowri
##Enter each subject marks - 10
##Enter each subject marks - 0
##Enter student name - Carl
##Enter each subject marks - 20
##Enter each subject marks - 0
##Student name = Gowri and marks = 10
##Student name = Gowri and marks = 0
##Student name = Carl and marks = 20
##Student name = Carl and marks = 0
#-------------------------------------------------

#Exercises
#1. Print multiplication tables of one chosen number (9 times table)
#2. Print multiplication tables of all the numbers from 1-12 
#3. Once done, take the inputs 1 and 12 from the user. Hence can be 20-30 time tables too
#4. Find the LCM of given two numbers
#5. Write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
#6. Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
