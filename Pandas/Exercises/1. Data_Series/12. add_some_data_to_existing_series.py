# 12. Write a pandas program to add some data to an existing Series

import pandas as pd

s = pd.Series(['100','200','python','300.12','400'])

print("Original Series: \n{}".format(s))
new_s = pd.concat([s,pd.Series([500,'php'])],ignore_index=True)

print("Adding new elements:\n{}".format(new_s))