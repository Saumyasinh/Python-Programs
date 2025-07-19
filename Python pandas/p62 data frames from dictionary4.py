import pandas as pd
import numpy as np

data={'Students':['Ram','Neha','Mansi'],'Marks':[22,33,44],'Sport':['Cricket','Football','Athelaics']}
df1=pd.DataFrame(data,index=['I','II','III'])
print(df1)