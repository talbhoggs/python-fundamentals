# What is panda?
# use for data analysis and manupulation
# make working with tabular data efficient

import pandas as pd

numbers = pd.Series([10, 20, 30])
print(numbers)
# -----------------------
# 0    10
# 1    20
# 2    30
# dtype: int64

data = {
    "Name":['Charles', 'Joy', 'Wil'],
    "Age":[44, 37, 7]
}

df = pd.DataFrame(data)
print(df)
# -----------------------
#     Name  Age
# 0  Charles   44
# 1      Joy   37
# 2      Wil    7


csv = pd.read_csv('ticket-list.csv')

print(csv.head())