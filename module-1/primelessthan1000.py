#prime no less than 1000

def prime(n):
    if(n<=1):
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True


for i in range(0,1000):
    if prime(i)==1:
        print(i,end=" ")
    