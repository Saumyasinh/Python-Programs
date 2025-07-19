import matplotlib.pyplot as plt
y=['One', 'Two', 'Three', 'Four', 'Five']
x=[15,24,35,50,20]
plt.barh(y,x)
plt.ylabel("Balls sold")
plt.xlabel("Price")
plt.title("Horizontal Bar Graph")
plt.show()