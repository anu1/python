import pandas as pd

first = pd.read_csv('in1.csv')
second = pd.read_csv('in2.csv')

merged = pd.merge(first, second, how='left', on='Num')
merged.to_csv('merged.csv', index=False)
