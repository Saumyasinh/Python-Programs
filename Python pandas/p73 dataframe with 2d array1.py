import pandas as pd
import numpy as np

staff=pd.Series([20,30,50])

salaries=pd.Series([40000,30000,25000])

avg=salaries/staff

org={'ppl':staff,'amount':salaries,'avg':avg}

df=pd.DataFrame(org)

print(df)