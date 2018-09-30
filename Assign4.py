#Q.1- Reverse the whole list using list methods.

lst=[45,90,'Python',22,'Table',10]
print(lst)
lst.reverse()
print(lst)

#Q.2- Print all the uppercase letters from a string.

s="The Princess in Black"
for i in s:
    if i==i.upper():
       print(i,end="")
print()

#Q.3- Split the user input on comma's and store the values in a list as integers.

lst=list(map(int,input("Enter the numbers:").split(",")))
print(lst)

#Q.4- Check whether a string is palindromic or not.

a=input("enter the string : ")
if (a==a[::-1]):
    print(a,'is a pallindrome')
else:
    print(a,'is not a pallindrome')

#Q.5- Make a deepcopy of a list
#write the difference between shallow copy and deep copy.

a=[3,'perl',4,'java',5]
b=a #shallowcopy
print("Original list a:",a,"id=",id(a))
print("shallow copy list b:",b,"id=",id(b))
del a[-1]
print("original list a:",a)
print("shallow copy list b:",b)

a=[3,'perl',4,'java',5,'python',7]
c=a.copy() #deepcopy
print("original list:",a,"id=",id(a))
print("Deep copy list:",c,"id=",id(c))

del a[-1]
print("original copy a:",a)
print("Deep copy list c:",c)

from copy import deepcopy
a=[3,'perl',4,'java',5,'python',7]
d=a.copy()#deepcopy
print("original list:",a,"id=",id(a))
print("Deep copy list:",d,"id=",id(d))

del a[-1]
print("original list a:",a)
print("shallow copy list d:",d)



    
