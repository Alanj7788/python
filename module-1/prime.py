#prime no within a certain range

def prime(n):
    if(n<=1):
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

print("Enter the range x to y:")
x=int(input("x:"))
y=int(input("y:"))

for i in range(x,y+1):
    if prime(i)==1:
        print(i,end=" ")
    