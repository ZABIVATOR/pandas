import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('flights.csv')
del df['Unnamed: 0']


df2 = df.groupby('CARGO').sum()


JumboPRICE=df2.iloc[0,0]
MediumPRICE=df2.iloc[1,0]
NimblePRICE=df2.iloc[2,0]
JumboWEIGHT=df2.iloc[0,1]
MediumWEIGHT=df2.iloc[1,1]
NimbleWEIGHT=df2.iloc[2,1]
Jumbo=0
Medium=0
Nimble=0

for i in range(650):
	if (df.loc[i,'CARGO']=='Jumbo'):
		Jumbo+=1
	if (df.loc[i,'CARGO']=='Medium'):
		Medium+=1
	if (df.loc[i,'CARGO']=='Nimble'):
		Nimble+=1

PRICE = {'Jumbo': JumboPRICE, 'Medium': MediumPRICE, 'Nimble': NimblePRICE }

bar_numbers = range(len(PRICE))
labels = list(PRICE.keys())
values = list(PRICE.values())

fig, ax = plt.subplots(1,3)

ax[1].bar(bar_numbers, values)
ax[1].set_xticks(bar_numbers)
ax[1].set_xticklabels(labels)
ax[1].set_title('PRICE')

WEIGHT = {'Jumbo': JumboWEIGHT, 'Medium': MediumWEIGHT, 'Nimble': NimbleWEIGHT }

bar_numbers2 = range(len(WEIGHT))
labels2 = list(WEIGHT.keys())
values2 = list(WEIGHT.values())

ax[2].bar(bar_numbers2, values2)
ax[2].set_xticks(bar_numbers2)
ax[2].set_xticklabels(labels2)
ax[2].set_title('WEIGHT')

n = {'Jumbo': Jumbo, 'Medium': Medium, 'Nimble': Nimble }
bar_numbers3 = range(len(n))
labels3 = list(n.keys())
values3 = list(n.values())

ax[0].bar(bar_numbers3, values3)
ax[0].set_xticks(bar_numbers3)
ax[0].set_xticklabels(labels3)
ax[0].set_title('NUMBER')

plt.show()


