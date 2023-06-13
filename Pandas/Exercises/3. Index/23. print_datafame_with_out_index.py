# 23. Write a pandas program to print datafame without index

import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'weight': [35, 32, 33, 30, 31, 32]},
     index =  [1, 2, 3, 4, 5, 6])
print("Original DataFrame with single index:")
print(df)

print("Data frame without index:")
print(df.to_string(index=False))