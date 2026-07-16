#Prime number check
n=int(input("Enter a number:"))

if(n==1 or n==0):
    print(" neither prime nor composite")

count=0;    
for i in range(2,n):
    if n%i==0:
        count=count+1

if(count>0):       
    print(n,"is a composite number")    
else:
    print(n,"is a prime number")    