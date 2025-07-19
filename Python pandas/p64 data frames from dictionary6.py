import pandas as pd
import numpy as np

abadsouth={'chalan':50,'amt':25000}
abadnorth={'chalan':70,'amt':75000}
abadeast={'chalan':100,'amt':50000}
abadwest={'chalan':10,'amt':5000}

totalchalan = [abadsouth,abadnorth,abadeast,abadwest]

df1 = pd.DataFrame(totalchalan,index=['abadsouth','abadnorth','abadeast','abadwest'])
print(df1)