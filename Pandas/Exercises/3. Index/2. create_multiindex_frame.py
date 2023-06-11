# 2. Write a pandas program to create a multinidex frame using two columns and using an index a column

import pandas as pd

df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
    't_id':['t1', 't2', 't3', 't4', 't5', 't6']})
print("Default Index:")
print(df.head(10))

# Multiindex
print("\n\nMultiindex using columns 't_id' and 'school_code")
df1 = df.set_index(['t_id','school_code'])
print(df1)

print("\n\nMultiindex using an index and a column")
df2 = df.set_index([pd.Index([0,1,2,3,4,5]),'t_id'])
print(df2)