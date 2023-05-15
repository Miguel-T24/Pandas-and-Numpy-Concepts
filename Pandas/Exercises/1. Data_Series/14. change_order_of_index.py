# 14. Write a pandas program to change the order of index of a given series

import pandas as pd

dic = {"A":1,"B":2,"C":3,"D":4,"E":5}
s = pd.Series(dic)
print("Original:\n{}".format(s))

s=s.reindex(index=['B','A','C','D','E'])
print("Reordered:\n{}".format(s))
