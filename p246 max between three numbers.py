no1=int(input("Enter no1 :"))
no2=int(input("Enter no2 :"))
no3=int(input("Enter no3 :"))
print("*"*30)
if(no1>=no2) and (no1>=no3):
    print(no1,"is greater")
elif (no2>=no1) and (no2>=no3):
    print(no2,"is greater")
else:
    print(no3,"is greater")
print("*"*30)