import pandas as pd
ser1=pd.Series([12,4,5,20,35])

print(ser1)

print(ser1.sort_values())

print(ser1.sort_values(ascending=False))