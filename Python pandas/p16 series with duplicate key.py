import pandas as pd
import numpy as np

a=np.arange(10,15)

s=pd.Series(data=a*2,index=['a','b','a','a','b'])

print(s)