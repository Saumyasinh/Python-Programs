data=[10,20,30,40,50,60]
no = len(data)
data.sort()
if no % 2==0:
    median1=data[no//2]
    median2=data[no//2-1]
    median=(median1 + median2)/2
else:
    median=data[no//2]
print("The median of the given numbers is",median)