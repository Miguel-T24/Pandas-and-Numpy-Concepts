# 4. Write a pandas program to add leading zeros to the character column in a pandas series and makes the length of th filed to 8 digit.

import pandas as pd
nums = {'amount': ['10', '250', '3000', '40000', '500000']}
print("Original dataframe:")
df = pd.DataFrame(nums)
print(df)

df['amount'] = df['amount'].apply(lambda x:'{:0>8}'.format(x))

print(df)