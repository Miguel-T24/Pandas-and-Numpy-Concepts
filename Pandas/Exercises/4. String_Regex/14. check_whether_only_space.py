# 14. Wrte a pandas program to check whether only space is present ina  given column of a datafme

import pandas as pd
df = pd.DataFrame({
    'company_code': ['Abcd','EFGF ', '  ', 'abcd', ' '],
    'date_of_sale ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})

print("Original DataFrame:")
print(df)

df['space'] = df['company_code'].apply(lambda x:x.isspace())

print(df)