# 41. Write a pandas program to remove the html tags within the specified column og a given dataframe

import pandas as pd
from re import sub

df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],
    'date_of_sale': ['12/05/2002','16/02/1999','05/09/1998','12/02/2022','15/09/1997'],
    'address': ['9910 Surrey <b>Avenue</b>','92 N. Bishop Avenue','9910 <br>Golden Star Avenue', '102 Dunbar <i></i>St.', '17 West Livingston Court']
})
print("Original DataFrame:")
print(df)


df['remove_html'] = df['address'].apply(lambda x:sub("<.*?>","",x))

print(df)