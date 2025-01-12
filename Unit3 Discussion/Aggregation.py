import numpy as np
import openpyxl
import pandas as pd
from pandas import read_csv, merge

coal_data = read_csv('/Users/mrkrinkle/Documents/Coding/Data Sets/School Datasets/Unit3 Discussion/Unit3 data/Range Global Coal Index.csv')
oil_data = read_csv('/Users/mrkrinkle/Documents/Coding/Data Sets/School Datasets/Unit3 Discussion/Unit3 data/Petrolium.csv')
water_data = read_csv('/Users/mrkrinkle/Documents/Coding/Data Sets/School Datasets/Unit3 Discussion/Unit3 data/AWK(American Water.csv')
copper_data = read_csv('/Users/mrkrinkle/Documents/Coding/Data Sets/School Datasets/Unit3 Discussion/Unit3 data/CPCPF(Copper).csv')

#coal calculations for change per day
coal_data.loc[:,'Daily Change'] = coal_data['Close']-coal_data['Open']

coal_mean = np.mean(coal_data['Daily Change'])
coal_std = np.std(coal_data['Daily Change'])
coal_cv = (coal_std/coal_mean)*100

#oil data
oil_data.loc[:,'Daily Change'] = oil_data['Close']-oil_data['Open']

oil_mean = np.mean(oil_data['Daily Change'])
oil_std = np.std(oil_data['Daily Change'])
oil_cv = (oil_std/oil_mean)*100

#water data
water_data.loc[:,'Daily Change'] = water_data['Close']-water_data['Open']

water_mean = np.mean(water_data['Daily Change'])
water_std = np.std(water_data['Daily Change'])
water_cv = (water_std/water_mean)*100

#copper data
copper_data.loc[:,'Daily Change'] = copper_data['Close']-copper_data['Open']

copper_mean = np.mean(copper_data['Daily Change'])
copper_std = np.std(copper_data['Daily Change'])
copper_cv = (copper_std/copper_mean)*100

#new df of all data
full_resource_aggregated = pd.concat([oil_data,coal_data,water_data,copper_data], ignore_index=True)
#save to new .csv
#full_resource_aggregated.to_csv("Unit3_Discussion_agg.csv",index=False)

#df for statistics
companies=['OILCF','AWK','COAL','CPCPF']
mean=[oil_mean,water_mean,coal_mean,copper_mean]
standard_deviation=[oil_std,water_std,coal_std,copper_std]
coef_variance=[oil_cv,water_cv,coal_cv,copper_cv]

Resources_stats = pd.DataFrame({'Companies':companies,'Mean':mean,'Standard Dev':standard_deviation,'Coefficient of Var':coef_variance,})
print(Resources_stats)

Resources_stats.to_csv('Res_stats.csv',index=False)