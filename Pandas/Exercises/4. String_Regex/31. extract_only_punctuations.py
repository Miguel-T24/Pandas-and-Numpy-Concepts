# 31. write a panas program tom extract inly punctuations from the specified column of a given Dataframe

import pandas as pd

pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'company_code': ['c0001.','c000,2','c0003', 'c0003#', 'c0004,'],
    'year': ['year 1800','year 1700','year 2300', 'year 1900', 'year 2200']
    })
print("Original DataFrame:")
print(df)

df['extract_punctuations'] = df['company_code'].str.findall("\W")

print(df)