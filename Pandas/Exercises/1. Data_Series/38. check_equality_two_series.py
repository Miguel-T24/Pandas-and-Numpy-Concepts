# 38. Write a pandas program to check the equality of two given series.

import pandas as pd
nums1 = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
nums2 = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])

print(nums1==nums2)