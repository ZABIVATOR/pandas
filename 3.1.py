import pandas as pd
import numpy as np

df1 = pd.read_csv('transactions.csv')
df2 = df1[df1['STATUS'] == 'OK']
print(df2)
df3 = df2.groupby('CONTRACTOR').sum()
print(df3.iloc[1,1])
m1=df1['SUM'].max()
print(m1)
df1 = df1.drop(df1[df1['SUM'] == m1].index)
m2=df1['SUM'].max()
print(m2)
df1 = df1.drop(df1[df1['SUM'] == m2].index)
m3=df1['SUM'].max()
print(m3)
