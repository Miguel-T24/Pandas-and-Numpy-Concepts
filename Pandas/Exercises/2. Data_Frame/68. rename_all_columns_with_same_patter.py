# 68. Write a pandas program to rename all columns with the same pattern of a given datarame.

import pandas as pd
df = pd.DataFrame({
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'],
    'date_of_birth': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': ['18', '21', '22', '22', '23']
})

print("Original:")
print(df)
df.columns = df.columns.str.lower().str.rstrip()
print("\nRemove trailing (at the end) whitesapce and convert to lowercase of the columns name")
print(df.head())