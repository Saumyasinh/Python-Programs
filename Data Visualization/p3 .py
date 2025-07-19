import matplotlib.pyplot as plt

bx=[50,100,150,200,250]
sy=[10,10,15,8,12]
by=[5,8,10,20,15]

plt.plot(bx,sy, label ="Small Balls")
plt.xlabel("Price")
plt.plot(bx,by, label="Big Balls")
plt.ylabel("Total Sales")
plt.legend()
plt.show()