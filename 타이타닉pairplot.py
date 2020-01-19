import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

#스타일 테마
sns.set_style('white')   # darkgrid, darkgrid, dark, white, ticks

titanic_pair = titanic[['age', 'pclass', 'fare']]

g = sns.pairplot(titanic_pair)

plt.show()
