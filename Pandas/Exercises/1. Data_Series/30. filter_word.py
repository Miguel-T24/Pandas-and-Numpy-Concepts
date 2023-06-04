# 30. Write a panda sprogram to filter word from  given that contain atleast two vowels

import pandas as pd

l = ['Red','Green','Orange','Pink','Yellow','White']
s = pd.Series(l)
print(s)

s1 = s.map(lambda x:len([i for i in x if i.lower() in list('aeiou')])>1)

print(s[s1])