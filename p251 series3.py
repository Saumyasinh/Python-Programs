n = int(input("Enter number =>"))
s=0
for i in range(1,n+1):
    print(i*i,"+", end="")
    s=s+i*i
print("\nsum =",s)

