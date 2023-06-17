# 30. Write a pandas program to extract only non alphanumeric characters from the specified column of a given dataframe

import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'company_code': ['c0001#','c00@0^2','$c0003', 'c0003', '&c0004'],
    'year': ['year 1800','year 1700','year 2300', 'year 1900', 'year 2200']
    })
print("Original DataFrame:")
print(df)

df['non_aphanumeric'] = df['company_code'].str.findall("(\W)+")
print(df)
