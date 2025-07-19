import pandas as pd

pd.set_option('display.max_rows',None)

titanic_data=pd.read_csv("titanic.csv",usecols=['Name','Age','Survived','Gender'])

data=titanic_data.loc[(titanic_data["Gender"]=='male')& (titanic_data["Age"]>35)]

print(data)