# 19. Write a apndas program to select a specific row of  given series datafme by integer index

import pandas as pd
ds = pd.Series([1,3,5,7,9,11,13,15], index=[0,1,2,3,4,5,7,8])
print("Original Series:")
print(ds)
print("\nPrint specified row from the said series using location based indexing:")
print("\nThird row:")
print(ds.iloc[[2]])
print("\nFifth row:")
print(ds.iloc[[4]])
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32]})

print("Original DataFrame with single index:")
print(df)
print("\nPrint specified row from the said DataFrame using location based indexing:")
print("\nThird row:")
print(df.iloc[[2]])
print("\nFifth row:")
print(df.iloc[[4]])