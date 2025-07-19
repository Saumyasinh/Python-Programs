import pandas as pd

titanic_data = pd.read_csv("titanic.csv")

data=titanic_data.loc[titanic_data["Age"]>30]

print(data)