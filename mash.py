import random

#introduction
print("Welcome to M.A.S.H! We will decide your future. Press enter after typing in each choice. Good luck!")

#setting up the lists
house = ['Mansion','Apartment', 'Shack', 'House']
spouse = ['','', '', '']
car = ['','', '', '']
kids = ['','', '', '']

#question one
print()
print("Enter the name of 4 people you would like to marry")
name1 = input("Name1: ")
spouse [0] = name1
name2 = input("Name2: ")
spouse [1] = name2
name3 = input("Name3: ")
spouse [2] = name3
name4 = input("Name4: ")
spouse [3] = name4

#question two
print()
print("Enter the name of 4 cars  you would like to drive")
car1 = input("Car1: ")
car [0] = car1
car2 = input("Car2: ")
car [1] = car2
car3 = input("Name3: ")
car [2] = car3
car4 = input("Car4: ")
car [3] = car4

#question three
print()
print("Enter your four favorite numbers")
Kid1 = input("Num1: ")
kids [0] = Kid1
Kid2 = input("Num2: ")
kids [1] = Kid2
Kid3 = input("Num3: ")
kids [2] = Kid3
Kid4 = input("Num4: ")
kids [3] = Kid4

print()
print("Thank you for playing.  Now we will be determining your future.")

#final verdict
print()
print ("You will live in a: ")
for i in range(1):
    print (house[i])
print ("You will be married to: ")
for i in range(1):
    print (spouse[i])
print ("You will drive a: ")
for i in range(1):
    print (car[i])
print ("You will have this many kids: ")
for i in range(1):
    print (kids[i])
print("Thanks for playing! Click the run button to play again.")
