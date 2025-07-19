import pandas as pd
import numpy as np

myarr=np.arange(1,21)
ser=pd.Series(myarr)
print(ser)

print(ser.nlargest(n=1))
print(ser.nsmallest(n=1))

print(ser.nlargest(n=3))
print(ser.nsmallest(n=3))