# 33. Write a pandas program to extract numbers greter than 940 from the specified column of a given dataframe

import pandas as pd
from re import findall
pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'address': ['7277 Surrey Ave.1111','920 N. Bishop Ave.','9910 Golden Star St.', '1025 Dunbar St.', '1700 West Livingston Court']
    })
print("Original DataFrame:")
print(df)

print("Numbers Greater tha 940")

def greater(string):
    l = findall("\d+",string)
    return " ".join(list(filter(lambda x:int(x)>940,l)))

df['greater_940'] = df['address'].apply(greater)
print(df)