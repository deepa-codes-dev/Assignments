#WAP to print multiplication table of a given number
a=int(input("Enter a number:"))
for i in range(1,11):
    print(a,"x",i,"=",a*i)


#Using while loop
n=int(input("Enter a number:"))
j=1
while(j<11):
    print(f"{n}x{j}={n*j}")
    j+=1
