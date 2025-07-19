import pandas as pd

ser=pd.Series(['a','a','a','b','b','c','d','e','e'])

print(ser.unique())
print(ser.nunique())