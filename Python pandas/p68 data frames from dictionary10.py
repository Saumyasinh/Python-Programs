import pandas as pd
data = [{'a':1,'b':2},{'a':5,'b':10,'c':20}]

df1=pd.DataFrame(data, index=['first','second'],columns=['a','b'])
print(df1)