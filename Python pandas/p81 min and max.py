import pandas as pd

titanic_data=pd.read_csv("titanic.csv")

print("Minimum")

print("*"*30)

print(titanic_data.min())

print("*"*30)

print("Maximum")

print("*"*30)
print(titanic_data.max())