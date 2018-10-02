#Q.1-  Take an input year from user.
#decide whether it is a leap year or not.

y=int(input("enter the year :"))
if (y%4==0):
    print(y,"is a leap year")
else:
    print(y,"is not a leap year")
print('-'*50)

#Q.2- Take length and breadth input from user.
#check whether the dimensions are of square or rectangle.

l=input("enter the length :")
b=input("enter the breadth :")
print(".....Well!!!")
if (l==b):
    print("This is a square.")
else:
    print("This is a rectangle.")
print('-'*50)

#Q.3- Take the input age of 3 people
#determine oldest and youngest among them.

x=34
y=20
z=51
if x>=y and x>=z:
    print(x,"is oldest")
elif y>=x and y>=z:
    print(y,"is oldest")
elif z>=x and z>=y:
    print(z,"is oldest")
else:
    print("All are equal")

print('-'*50)

#Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N )
#then using following rules print their place of service. 
#1. if employee is female, then she will work only in urban areas. 
#2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
#3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
#4. And any other input of age should print "ERROR".

a=int(input("enter your age :"))
s=input("enter your sex(M or F): ")
m=input("marital status-married(Y or N):")
if (s=="F")and(20<a<60):
    print("You will work in urban areas")
elif (s=="M") and (20<a<40):
    print("You will work anywhere")
elif (s=="M") and (40<a<60):
    print("You will work in urban areas only")
else:
    print("!!! ERROR !!!")

print('-'*50)

#Q.5- A shop will give discount of 10%
#if the cost of purchased quantity is more than 1000.
#Ask user for quantity Suppose,
#one unit will cost 100.
#Judge and print total cost for user.
q=int(input("Enter the quatity of the product you want :"))
if (q*100 > 1000):
    print("the user gets 10% discount")
    print("total cost is :",((q*100)-q*100*.1))
else:
    print("No discount..")
print('-'*50)

   #LOOPS
#Q.1- Take 10 integers from user and print it on screen.
l=[]
for a in range(10):
    integer=int(input("enter the no: "))
    l.append(integer)
print(l)
for b in l:
    print(b)
print('-'*50)      
#Q.3- Create a list of integer elements by user input.
#Make a new list which will store square of elements of previous list.
lst=list(map(int,input("enter the elements :")))
lst_square=[]
for i in lst:
    lst_square.append(i**2)
print(lst_square)

print('-'*50)

#Q.4- From a list containing ints, strings and floats,
#make three lists to store them separately
l=["apple",2,4,6,2.5,"java","perl",4.99]
l_int=[]
l_float=[]
l_string=[]
for i in l:
    if type(i)==int:
        l_int.append(i)
    elif type(i)==float:
        l_float.append(i)
    else:
        l_string.append(i)
print(l_int)
print(l_float)
print(l_string)
    
print('-'*50)

#Q.5- Using range(1,101),
#make a list containing only prime numbers.
num=[]
for i in range(1,101):
    flag= False
    for j in range(2,i):
        if i%j==0:
            flag= True
    if not flag:
        num.append(i)
print(num)
print('-'*50)
#Q.6-  Print the following patterns: 
#* 
#** 
#*** 
#**** 
def printstar(symbol,n):
     count=1
     while count<=n:
         print(symbol*count)
         count=count+1
     return
printstar('*',5)

#Q.7- Take inputs from user to make a list.
#Again take one input from user and
#search it in the list and
#delete that element, if found.
#Iterate over list using for loop.
l=list(map(int,input("enter list elements:").split()))
element=int(input("enter the elements to search: "))
if element in l:
    print("element found")
    del l[l.index(element)]
print(l)

#Q.2- Write an infinite loop.An infinite loop never ends.
#Condition is always true.
while True:
    print("infinite")
print('-'*50)

    
