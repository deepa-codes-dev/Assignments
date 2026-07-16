#factorial of a number using for loop

a=int(input("Enter a non-negative number"))

fact=1
for i in range(1,a+1):
    fact=fact*i
print("The factorial of",a,"is",fact)    