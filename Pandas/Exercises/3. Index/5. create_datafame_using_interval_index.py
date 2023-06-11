# 5. Write a pandas program to crate a dataframe using intervals as an index.

import pandas as pd

print("Create an interval index using intervalindex.from_breaks")

df_interval = pd.DataFrame({"X":[1, 2, 3, 4, 5, 6, 7]}, 
                           index = pd.IntervalIndex.from_breaks(
                               [0,0.5,1.0,1.5,2.0,2.5,3,3.5]
                           ))

print(df_interval)