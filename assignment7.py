#1
a=3
if a<4:
    try:
        a=a/(a-3)
    except ZeroDivisionError as ob:
        print(ob)
print('-'*50)
#2
try:
    l=[1,2,3]
    print(l[3])
except IndexError as bj:
    print(bj)
print('-'*50)
#3
try:
    raise NameError("hi there")
except NameError:
    print("an exception")
    raise
print('-'*50)
#4
def AbyB(a,b):
    try:
       c=((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b result in 0")

    else:
        print(c)

AbyB(2.0,3.0)
AbyB(3.0,3.0)
print('-'*50)
#5
import sys
try:
    from time import datetime
except Exception as e:
    print(e)

while True:
    try:
        x=int(input("Enter a number: "))
        break
    except ValueError:
        print("That was not a valid number. Try again..!")
x=[34,76,56]
try:
    for i in range(5):
        print(x[i])
except IndexError as ab:
       print(ab)
print('-'*50)
