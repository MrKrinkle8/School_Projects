import pandas as pd
import matplotlib.pyplot as plt
from pandas import read_csv

data = read_csv("/Users/mrkrinkle/Documents/Coding/Data Sets/School Datasets/Unit2 Discussion/WVS_Cross-National_Wave_7_csv_v6_0.csv")

filtered_data= data[data['B_COUNTRY_ALPHA'].isin(['USA','DEU'])]
filtered_data= filtered_data[filtered_data['Q275R'].isin([1,2,3])]

Freq_table = pd.crosstab(filtered_data['Q275R'],filtered_data['B_COUNTRY_ALPHA'])
Freq_table.plot(kind='bar',figsize=(10,6))

plt.xlabel('Answers')
plt.ylabel('Count per Country')
plt.title('Education levels for USA and Germany')
plt.legend(title='Country')
plt.xticks([0,1,2],['Lower Education','Middle Education', 'Higher Education'], rotation=0)
plt.show()