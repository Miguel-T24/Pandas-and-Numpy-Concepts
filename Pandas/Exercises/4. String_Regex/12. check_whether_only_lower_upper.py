# 12. Write a pandas program to check whether only lower case or upper case is present in a given column of datframe

import pandas as pd
df = pd.DataFrame({
    'company_code': ['ABCD','EFGF', 'hhhh', 'abcd', 'EAWQaaa'],
    'date_of_sale ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})

print("Original DataFrame:")
print(df)

df['lower_upper'] = df['company_code'].apply(lambda x:("Upper","Lower")[x.islower()])

print(df)