n=int(input("Enter no. of rows:(n<=26):"))
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
if n>26:
    print("Error")
else:
    for i in range(n):
        for j in range(i+1):
            print(letters[j],end="")
        print()
    