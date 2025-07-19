import pandas as pd
my_dict={'Name':["Omkar","Bijav","Dhiren","Pranali","Keval"],'Age':[10,20,30,40,50],'Designation':["CEO","VP","SVP","AM","DEV"]}
df=pd.DataFrame(my_dict,index=["First ->","Second ->","Third ->","Four ->","Five ->"])
print(df)