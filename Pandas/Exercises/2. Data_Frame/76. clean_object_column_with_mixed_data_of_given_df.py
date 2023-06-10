# 76. Write a pandas program to clean object column with mixed of a given data frame using regular expression

import pandas as pd
d = {"agent": ["a001", "a002", "a003", "a003", "a004"], "purchase":[4500.00, 7500.00, "$3000.25", "$1250.35", "9000.00"]}
df = pd.DataFrame(d)
print("Original dataframe:")
print(df)

print("\nData Types:")
print(df["purchase"].apply(type))
df["purchase"] = df["purchase"].replace("[$,]", "", regex = True).astype("float")
print("\nNew Data Types:")
print(df["purchase"].apply(type))   