# 35. Write a pandas program to check whether two given word present in a specified column of a given dataframe

import pandas as pd


pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'address': ['9910 Surrey Ave.','92 N. Bishop Ave.','9910 Golden Star Ave.', '102 Dunbar St.', '17 West Livingston Court']
    })
print("Original DataFrame:")
print(df)

print("9910 and Ave present in column address:")

def two_words(st):
    st = st.split(" ")
    return " ".join(st) if ("9910" in st and "Ave." in st) else ""

df['Two_words'] = df['address'].apply(two_words)

print(df)