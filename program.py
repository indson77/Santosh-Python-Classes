# Questions: 4, 15,16,18, 21, 24, 30 


# 4 area of the circle 
radius_of_circle = int(input("enter the radius of circle : "))
area = 3.14*radius_of_circle*radius_of_circle 
print(area)

# 16 diffrence from 17 
num_ = int(input("enter your number : "))
sub_ = 17 - num_
if num_ > 17 :
    print(sub_*2)
else :
    print(sub_)

# 15 volume of sphere of radius 6 
radius = int(input("enter the radius of sphere :"))
surface_area = 4/3*3.14*radius**3
if radius == 6 :
    print(surface_area)
else :
    print("write radius value equal to 6 ")

# 18 sum of three number
a = int(input("entar your first value :"))
b = int(input("enter your second value :"))
c = int(input("enter you third value :"))
sum = a + b + c
if a == b == c :
    print(sum*3)
else :
    print(sum)

# 21 even or odd checker 
value_ = int(input("enter your value"))
if value_%2 == 0 :
    print("the given no is even number")
else :
    print("the given no is odd number")

# 24 vowel tester 
letters = input("enter the any letter whatever you want :")
if letters == 'a':
    print("letter is vowel")
elif letters == 'e':
    print("letter is vowel")
elif letters == 'i':
    print("letter is vowel")
elif letters == 'o':
    print("letter is vowel")
elif letters == 'u':
    print("letter is vowel")
else:
    print("letter is consonant") 

# 30 area of triangle 
base = int(input("enter the value of base of triangle :"))
height = int(input("enter the height of the triangle :"))
area_of_triangle = 1/2*base*height
print("area of triangle = ", area_of_triangle)  