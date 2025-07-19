import pandas as pd
import numpy as np

a=np.arange(10,20)

s = pd.Series(index=a,data=a*2)

print(s)