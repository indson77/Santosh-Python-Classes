#1 even or odd checker 
odd_eve = int(input("enter your value : "))
if odd_eve % 2 == 0 :
    print("the given number is even")
else :
    print("the given no is odd")

#2 to check the given no is positive,negative or zero
num = int(input("enter you value :"))
if num > 0 :
    print("the given no is positive")
elif num < 0 :
    print("the given no is negative")
else :
    print("the given is zero")

#3 largest of two number 
first = int(input("enter your first number :"))
second = int(input("enter your second number :"))
if first > second :
    print("first number is the largest one")
else :
    print("second number is the largest one")

#4 leap year checker 
year = int(input("enter the year :"))
if year % 4 == 0 :
    print("this is the leap year")
else :
    print("this is not the leap year")

#6 eligible to vote or not 
age = int(input("enter your age :"))
if age >= 18 :
    print("you are eligible to vote")
else :
    print("you are not eligible to vote")

#7 grade calculator 
marks = int(input("enter your marks :"))
if marks >= 90 and marks <= 100 :
    print("grade : A ")
elif marks >= 80 and marks <=89 :
    print("grade : B ")
elif marks >= 70 and marks <= 79 :
    print("grade : C ")
elif marks >= 60 and marks <= 69 :
    print("grade : D ")
elif marks <60 and marks>= 0 :
    print("grade : E")
else :
    print("pls enter the valid marks ")

#8 try checker 
num = int(input("enter your number :"))


