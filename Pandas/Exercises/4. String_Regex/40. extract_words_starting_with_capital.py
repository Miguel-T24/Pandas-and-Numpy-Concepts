# 40. Write a pandas program to extract words strating with capital words from a given column of a given dataframe

import pandas as pd

df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],
    'date_of_sale': ['12/05/2002','16/02/1999','05/09/1998','12/02/2022','15/09/1997'],
    'address': ['9910 Surrey Avenue','92 N. Bishop Avenue','9910 Golden Star Avenue', '102 Dunbar St.', '17 West Livingston Court']
})

print("Original DataFrame:")
print(df)

def if_capital(string):
    string = string.split()
    return " ".join(list(filter(lambda x:x.istitle(),string)))

df['extract_capital_words'] = df['address'].apply(if_capital)
print(df)