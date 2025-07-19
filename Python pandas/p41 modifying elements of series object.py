import pandas as pd

ser1=pd.Series([12,34,45,50,24])

ser1[0]=2200
print(ser1)

ser1[0:3]=1200
print(ser1)