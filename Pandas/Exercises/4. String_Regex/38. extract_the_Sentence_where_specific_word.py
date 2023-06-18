# 38. Write a pandas program to extract the sentence where a specific word is present in a given column of a given dataframe

import pandas as pd

df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],
    'date_of_sale': ['12/05/2002','16/02/1999','05/09/1998','12/02/2022','15/09/1997'],
    'address': ['9910 Surrey Avenue','92 N. Bishop Avenue','9910 Golden Star Avenue', '102 Dunbar St.', '17 West Livingston Court']
})
print("Original DataFrame:")
print(df)

def if_contain(string):
    string = string.split()
    return " ".join(string) if "Avenue" in string else ""

df['filter'] = df['address'].apply(if_contain)

print(df)