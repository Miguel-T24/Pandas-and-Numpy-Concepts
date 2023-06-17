# 27. Write a pandas program to extract inly number from the specified column of given datafme

import pandas as pd

pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'address': ['7277 Surrey Ave.','920 N. Bishop Ave.','9910 Golden Star St.', '25 Dunbar St.', '17 West Livingston Court']
    })
print("Original DataFrame:")
print(df)

df['number'] = df['address'].str.extract("(\d+)",expand=True)
print(df)