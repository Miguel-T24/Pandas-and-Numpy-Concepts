# 36. Write a pandas program to extract date (format: mm-dd-yyyy) from a given column of a given dataframe

import pandas as pd
# from re import sub

df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],
    'date_of_sale': ['12/05/2002','16/02/1999','05/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]
})
print("Original DataFrame:")
print(df)

print("new date")

# df["format_date"] = df['date_of_sale'].apply(lambda x: sub("/","-",x))
df["format_date"] = df['date_of_sale'].apply(lambda x: x.replace('/',"-"))

print(df)