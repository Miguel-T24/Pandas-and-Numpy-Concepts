# 39. Write a pandas program to fin the index of the first occurence of the smalles and largest value of a given series

import pandas as pd
nums = pd.Series([1, 3, 7, 12, 88, 23, 3, 1, 9, 0])
print("Original Series:")
print(nums)

print(pd.Index(nums).get_loc(min(nums)))
print(pd.Index(nums).get_loc(max(nums)))

print(nums.idxmin())
print(nums.idxmax())