import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

#스타일 테마

sns.set_style('darkgrid') #darkgrid, whitegrid, dark, white, ticks)

fig = plt.figure(figsize = (15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

sns.regplot(x='age', y='fare', data=titanic, ax = ax1)
sns.regplot(x='age', y='fare', data=titanic, ax = ax2, fit_reg=False)

# 피벗 테이블로 범주형 변수를 행, 열로 재구분, 정리

table = titanic.pivot_table(index = ['sex'], columns=['class'], aggfunc='size')

sns.heatmap(table, annot=True, fmt = 'd', cmap = 'YlGnBu', linewidth = 5, cbar = False)

plt.show()


####seaborn.box####
