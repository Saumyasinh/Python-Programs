import pandas as pd
import numpy as np

ar=np.array([[20000,30000,50000],[420,310,250],[121,200,30]])

df=pd.DataFrame(ar,columns=['ppl','hospital','schools'],index=['delhi','mumbai','surat'])

print(df)

print("Only ppl")
print(df.ppl)

print("Only hospital")
print(df.hospital)

print("hospital schools")
print(df[["schools","hospital"]])