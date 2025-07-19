import matplotlib.pyplot as plt
y=['onr','two','three','four','five']

sball=[15,24,35,50,20]
bball=[10,15,30,25,50]

plt.barh(y,sball)
plt.barh(y,bball)

plt.ylabel("Balls Sold")
plt.xlabel("Price")
plt.title("Horizontal Bar Graph :Balls Sold")
plt.legend(['Small Balls', 'Big Balls'])
plt.show()