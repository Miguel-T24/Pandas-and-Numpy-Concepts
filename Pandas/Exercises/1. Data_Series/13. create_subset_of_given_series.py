# 13. Write a pandas program to crate a subset of a given series based on value and condition

import pandas as pd

s = pd.Series(list(range(11)))
print("Original: \n{}".format(s))

sub = s[s<6]
print("Subset:\n{}".format(sub))
