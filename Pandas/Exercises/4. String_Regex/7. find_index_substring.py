# 7. Write a apndas program to find the index of a given substring of a datafame oclumn

import pandas as pd
df = pd.DataFrame({
    'name_code': ['c001','c002','c022', 'c2002', 'c2222'],
    'date_of_birth ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'age': [18.5, 21.2, 22.5, 22, 23]
})
print("Original DataFrame:")
print(df)
print("\nCount occurrence of 22 in date_of_birth column:")
df['Index'] = df['name_code'].apply(lambda x:x.find('22'))
print(df)