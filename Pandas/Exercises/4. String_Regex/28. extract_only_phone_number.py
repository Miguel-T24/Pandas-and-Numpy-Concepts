# 28. Write a pandas program to extract only phone number from the specified column og a given dataframe

import pandas as pd
pd.set_option('display.max_columns', 10)

df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'company_phone_no': ['Company1-Phone no. 4695168357','Company2-Phone no. 8088729013','Company3-Phone no. 6204658086', 'Company4-Phone no. 5159530096', 'Company5-Phone no. 9037952371']
    })
print("Original DataFrame:")
print(df)

df['phone_number'] = df['company_phone_no'].str.extract("(\d{2,})",expand=True)

print(df)