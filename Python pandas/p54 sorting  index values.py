import pandas as pd
ser1=pd.Series([12,4,5,20,35],index=['b','d','a','c','e'])

print(ser1)

print("\n",ser1.sort_index())

print("\n",ser1.sort_index(ascending=False))