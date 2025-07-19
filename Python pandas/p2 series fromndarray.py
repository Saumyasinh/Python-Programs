import pandas as pd
import numpy as np

array=['a','b','c','d','e']
data = np.array(array)

ser = pd.Series(data)
print(ser)