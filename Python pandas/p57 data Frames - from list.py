import pandas as pd

data = [['Alexa',10],['Vihaan',12],['Rani',13],['Vedika',13]]

df = pd.DataFrame(data,columns=['Name','Age'])

print(df)