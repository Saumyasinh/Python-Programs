n = int(input("Enter number =>"))
s=0
for i in range(1,n+1):
    if i%2==0:
        print(i , "-", end="")
    else:
        print(i , "+", end="")
s=s+i
print("\n sum =",s)