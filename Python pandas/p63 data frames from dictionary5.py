import pandas as pd
import numpy as np

ranker1={'Rno':12,'Name':'Ram','Marks':99}
ranker2={'Rno':2,'Name':'Raj','Marks':97}
ranker3={'Rno':32,'Name':'Nisha','Marks':95}
ranker4={'Rno':40,'Name':'Ravi','Marks':94}

rankers=[ranker1,ranker2,ranker3,ranker4]
df1=pd.DataFrame(rankers,index=['I','II','III','IIII'])
print(df1)