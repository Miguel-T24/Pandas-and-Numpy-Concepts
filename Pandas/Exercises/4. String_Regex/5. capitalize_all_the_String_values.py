# 5. Write a pandas program tom capitalize all the string values of specified columns of a given dataframe

import pandas as pd

df = pd.DataFrame({
    'name': ['alberto','gino','ryan', 'Eesha', 'syed'],
    'date_of_birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [18.5, 21.2, 22.5, 22, 23]
})

print("Original DataFrame:")
print(df)
print(df.info())

df['name'] = df['name'].apply(lambda x:x.capitalize())
print(df)