# 33. Write a pandas program to replace missing white spaces in a given with the least frequent character


str1 = "abc def abcdef icd"

# Way 1: Collections
from collections import Counter
str_temp = Counter(str1)
print(str_temp.most_common()[-1][0])
lea_com = str_temp.most_common()[-1][0]
r = str1.replace(" ",lea_com)
print(r)

#  Way 2: Pandas Series
import pandas as pd
s = pd.Series(list(str1))
print(s)
s = s.map(lambda x:lea_com if (x==" ") else x)
print(s)
print("".join(s))

# way 3: only pandas
print("\n\nLast way\nOriginal Series:")
print(str1)
s = pd.Series(list(str1))
print(s)
el_freq = s.value_counts()
print(el_freq)
current_freq = el_freq.dropna().index[-1]
print(current_freq)
result = "".join(s.replace(" ",current_freq))
print(result)