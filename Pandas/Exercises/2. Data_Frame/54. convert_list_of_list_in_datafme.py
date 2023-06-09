# 54. Write a pandas proram to convert a given list of list into a datafame

import pandas as pd

list_list = [[2, 4], [1, 3]]
col = ['col1','col2']

df = pd.DataFrame(list_list,columns=col)

print(df)