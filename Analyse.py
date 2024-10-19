import pandas as pd

df = pd.read_csv("police.csv")
df.head()

import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
import seaborn
seaborn.histplot(data=df , x='driver_age')
plt.show()

plt.figure(figsize=(12,6))
seaborn.scatterplot(data=df, x='driver_age', y= 'stop_duration')
plt.show()


race_duration =df ['draver_race'].value_counts()
plt.figure(figsize=(12,6))
plt.pie(race_duration, labels=race_duration.index, autopct = '')
plt.title("распределение расс")
plt.show()

df['stop_date'] = pd.to_datetime(df['stop_date'])
df.info()

df['year_month'] = df['stop_date'].dt.to_period("M")
df.head()

mounthly_stats = df.groupby('year_month').size()
mounthly_stats.plot(kind='bar')
plot.show()


import seaborn as sns

plt.figure(figsize=(12,6))
correlation = df[['driver_age','is_arrested','stop_date']].corr()
sns.heatmap(correlation, annot=True,fmt = '.2f', cmap = 'coolwarm', square = True)

