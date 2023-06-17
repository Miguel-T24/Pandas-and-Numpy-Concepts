# 13. Write a pandas program to check whether only proper case or title case is present in a given column of datarame

import pandas as pd
df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'Hhhh', 'abcd', 'EAWQaaa'],
    'date_of_sale ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})

print("Original DataFrame:")
print(df)

df['Title_Case'] = df['company_code'].apply(lambda x:"Title Case" if x.istitle() else "NO Title")

print(df)