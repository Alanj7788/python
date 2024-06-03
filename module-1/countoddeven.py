# numbers=[int(x) for x in input("Enter numbers seperated by spaces: ").split() ]
# or take input as

n=int(input("Enter n:"))
numbers= [int(input()) for i in range(n) ]
print(numbers)
odd=0;even=0
for i in numbers:
    if i%2==1:
        odd+=1
    else:
        even+=1
print("odd count:",odd)
print("even count:",even)