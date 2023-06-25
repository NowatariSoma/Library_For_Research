import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv('csv_input/practice.csv')

subset = df['D']

list_data = subset.values.tolist()
print(list_data)