# 16. Write a pandas program to get the items of a given series not present in another given series

import pandas as pd

sr1 = pd.Series([1,2,3,4,5])
sr2 = pd.Series([2,4,8,10])

print("Series 1:\n{}".format(sr1))
print("Series 2:\n{}".format(sr2))


sr3 = sr1[~sr1.isin(sr2)]
print("Series 3: \n{}".format(sr3))
