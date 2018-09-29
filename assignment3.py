#Q.1- Create a list with user defined inputs
lst=list(input('enter the elements:').split())
print(lst)

#Q.2- Add the following list to above created list: 
#[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]
a=lst+['google','apple','facebook','microsoft','tesla']
print(a)

#Q.3- Count the number of time an object occurs in a list.
b=['google','apple','facebook','microsoft','tesla','apple']
print(b)
print(b.count('apple'))

#Q.4- Create a list with numbers and sort it in ascending order.

lst=[10,55,2,77,87,43,90]
print(lst)
lst.sort()
print(lst)

#Q.5- Given are two one-dimensional arrays A and B which are sorted in ascending order.
#Write a program to merge them into a single sorted array C
#that contains every item from arrays A and B, in ascending order. [List]
A=[2,4,6,8,10]
B=[4,8,12,20,24]
C=A+B
C=sorted(C)
print(C)

#Q.6- Count even and odd numbers in the list.
a=[3,12,5,67,44,34,23]
print(a)
no_even=0
no_odd=0
for i in a:
    if i%2==0:
        no_even +=1
    else:
        no_odd +=1
print("count of even no: "+str(no_even))
print("count of odd no: "+str(no_odd))

#Q.7- Print a tuple in reverse order.
tup=(23,56,89,12)
print(tup[::-1])

#Q.8- Find largest and smallest elements of a tuples.
tup=(2,4,6,8,10)
print("largest:",max(tup),"smallest:",min(tup))

#Q.9- Convert a string to uppercase.
str="The princess in black"
print(str.upper())

#Q.10-  Print true if the string contains all numeric characters.
str="65,32,11,67,22"
print(str.isnumeric())

#Q.11- Replace the word "World" with your name in the string "Hello World".
a="Hello World"
b=a.replace('World','Niharika')
print(b)


