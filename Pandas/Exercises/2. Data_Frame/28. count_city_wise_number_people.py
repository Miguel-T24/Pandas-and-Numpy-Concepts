# 28. Write a pandas program to count city wise number of people from a given of data set (city, name of the person).

import pandas as pd

df1 = pd.DataFrame({
'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'city': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles']})
print(df1)



g1 = df1.groupby(["city"]).size().reset_index(name='Number of people')
print(g1)