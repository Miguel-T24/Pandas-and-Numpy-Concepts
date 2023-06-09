# 49. Write a pandas program to append data to an empty dataframe

import pandas as pd


df = pd.DataFrame()
print(df)

df["col1"] = [0,1,2]
print(df)
df["col2"] = [0,1,2]
print(df)

data = pd.DataFrame({"col3":range(3),'col4':range(3)})
df = df.append(data)
print(df)