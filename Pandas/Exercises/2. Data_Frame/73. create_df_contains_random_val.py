# 73. Write a pandas program to crate dataframes that contains random values, contains missing values, contains datatime values and contains mixed values

import pandas as pd
print("DataFrame: Contains random values:")
df1 = pd.util.testing.makeDataFrame() # contains random values
print(df1)
print("\nDataFrame: Contains missing values:")
df2 = pd.util.testing.makeMissingDataframe() # contains missing values
print(df2)
print("\nDataFrame: Contains datetime values:")
df3 = pd.util.testing.makeTimeDataFrame() # contains datetime values
print(df3)
print("\nDataFrame: Contains mixed values:")
df4 = pd.util.testing.makeMixedDataFrame() # contains mixed values
print(df4)