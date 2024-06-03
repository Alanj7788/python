def fact(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    return factorial
n=int(input("enter n:"))
x=int(input("Enter x:"))
sum=0
j=0
for i in range(n):
    if i%2==0:
        sum=sum+((x**j)/fact(j))
    else:
        sum=sum-((x**j)/fact(j))
    j=j+2
print(sum)
