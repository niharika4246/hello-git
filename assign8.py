#functions.
# calculate the area of square.
print("Enter 'x' for exit.");
side = input("Enter side length of Square: ");
if side == 'x':
    exit();
else:
    side_length = int(side);
    area_square = side_length*side_length;
    print("\nArea of Square =",area_square);
print('-'*20)
#print all the perfect numbers b/w 1 to 1000
limit = int(input("enter upper limit for perfect number search: "))

n = 1

while n <= limit:

    sum = 0
    divisor = 1
    while divisor < n:
        if not n % divisor:
            sum += divisor
        divisor = divisor + 1
    if sum == n:
        print(n, "is a perfect number")
    n = n + 1
print('-'*20)    
#print a multiplication table of a user defined number.
num=int(input("enter a number:"))
for i in range(1,10):
    print(num,'x',i,'=',num*i)
print('-'*20)    
#calculate power of a number using recursion.
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))
