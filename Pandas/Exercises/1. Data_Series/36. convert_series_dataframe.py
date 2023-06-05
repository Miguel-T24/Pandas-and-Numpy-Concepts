# 36. Write a python program to convert given series into a datafme with its index as anohter columnn on the dataframe

import pandas as pd

char_list = 'ABCDEFGH'
num_array = list(range(8))

print(char_list)
print(num_array)

num_dict = dict(zip(char_list,num_array))
print(num_dict)

num_ser = pd.Series(num_dict)
print(num_ser)

df = num_ser.reset_index()
print(df)