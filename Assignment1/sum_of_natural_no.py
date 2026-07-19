#Sum of n natural numbers using for loop
a=int(input("Enter a number:"))
s=0
for i in range(1,a+1):
    s=s+i
print("The sum is:",s)    


#Using while loop
a=int(input("Enter a number:"))
i=1
s=0
while(i<=a):
    s=s+i
    i=i+1
print("The sum is",s)    