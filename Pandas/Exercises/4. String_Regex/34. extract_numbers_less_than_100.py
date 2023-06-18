# 34. Write a pandas program to extract numbers less than 100 from the specified column of a given dataframe

import pandas as pd
from re import findall

df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'address': ['72 Surrey Ave.11','92 N. Bishop Ave.','9910 Golden Star St.', '102 Dunbar St.', '17 West Livingston Court']
    })
print("Original DataFrame:")
print(df)

def less_100(s):
    l = findall('\d+',s)
    l = list(filter(lambda x:int(x)<100,l))
    return " ".join(l)

df['less_than_100'] = df['address'].apply(less_100)
print(df)