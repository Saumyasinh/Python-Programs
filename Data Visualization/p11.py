import matplotlib.pyplot as plt
x=["Mango","Banana","Orange","Guava","Grapes"]
y=[400,350,250,200,550]
plt.bar(x,y)
plt.bar(x,y,color="Orange")

plt.xlabel("FRUITS")
plt.ylabel("PRICE/KG")
plt.title("Fruits and their Prices/kg")
plt.show()