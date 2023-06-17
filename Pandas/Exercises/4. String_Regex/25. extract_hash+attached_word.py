# 25. Write a pandas program to exrtact hash attached word from twitter text from the specified column of a given dataframe

import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'tweets': ['#Obama says goodbye','Retweets for #cash','A political endorsement in #Indonesia', '1 dog = many #retweets', 'Just a simple #egg']
    })
print("Original DataFrame:")
print(df)

print("\n\nExtracting # word from datarfame")

df['Hashtag'] = df['tweets'].str.extract("(#\w+)",expand=True)
print(df)