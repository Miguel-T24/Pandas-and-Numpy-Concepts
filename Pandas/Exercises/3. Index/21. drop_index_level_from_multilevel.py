# 21. Write a panda sprogram to drop a index level from multilevel column index of a datarfame

import pandas as pd
cols = pd.MultiIndex.from_tuples([("a", "x"), ("a", "y"), ("a", "z")])
print("\nConstruct a Dataframe using the said MultiIndex levels: ")
df = pd.DataFrame([[1,2,3], [3,4,5], [5,6,7]], columns=cols)
print(df)
#Levels are 0-indexed beginning from the top.
print("\nRemove the top level index:")
df.columns = df.columns.droplevel(0)
print(df)
df = pd.DataFrame([[1,2,3], [3,4,5], [5,6,7]], columns=cols)
print("\nOriginal dataframe:")
print(df)
print("\nRemove the index next to top level:")
df.columns = df.columns.droplevel(1)
print(df)