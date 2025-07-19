import numpy as np
import pandas as pd

d = {'Surat':pd.Series([2., 3., 4.],index=['2000','2001','2002']),'Mumbai':pd.Series([2., 3., 4., 5.],index=['2000','2001','2002','2003'])}
df = pd.DataFrame(d)
print(df)
df=pd.DataFrame(d,index=['2000','2001'])
print(df)