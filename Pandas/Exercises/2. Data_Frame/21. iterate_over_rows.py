# 21. Write a pandas program to iterate over rows in datafame

import pandas as pd

exam_data = [{'name':'Anastasia', 'score':12.5}, {'name':'Dima','score':9}, {'name':'Katherine','score':16.5}]

df = pd.DataFrame(exam_data)
print(df)

print("Iteration")

for i ,r in df.iterrows():
    print(r['name'],r['score'])