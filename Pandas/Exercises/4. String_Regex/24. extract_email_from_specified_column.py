# 24. Write a pandad program to extract email from specified column of stirng type of given dataframe

import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'name_email': ['Alberto Franco af@gmail.com','Gino Mcneill gm@yahoo.com','Ryan Parkes rp@abc.io', 'Eesha Hinton', 'Gino Mcneill gm@github.com']
    })
print("Original DataFrame:")
print(df)

print("\nEmail of column")
df['email'] = df['name_email'].str.extract('([A-Za-z]+@[A-Za-z]+.com)', expand=True)

print(df)