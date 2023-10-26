#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 15:49:54 2022

@author: btang1
"""


import numpy as np
import fnmatch
from netCDF4 import Dataset
import codecs
import datetime
from datetime import datetime as dt
import pandas as pd
import statistics as stat

'''
1) read in excel data
'''
file_loc = '/Volumes/Ext_Disk_1/3_NOAA_projects/NOAA_cmaq_project/beiming_code/score_card/'
filename = 'US_interpolated_AQS_PM25'
obs_df = pd.read_excel(file_loc+filename+'.xls')
pd.set_option('display.max_columns',None)  
    
Date = list(obs_df['Date'])
LOC_NUMBER = list(obs_df['Location_number'])
AQS_OBS_PM25 = list(obs_df['AQS_OBS_PM25'])
MODEL_V52_PM25 = list(obs_df['MODEL_V52_PM25'])
MODEL_V54_PM25 = list(obs_df['MODEL_V54_PM25'])
States = list(obs_df['STATES'])
Land_use_cover = list(obs_df['LAND_USE_COVER'])
Urban = list(obs_df['URBAN'])
'''
2) Group by states, urban, & date
'''
arrays = [States,Urban,Date ]
index = pd.MultiIndex.from_arrays(arrays,names=('States','Urban','Date'))
df_aqs = pd.DataFrame({'AQS obs pm2.5': AQS_OBS_PM25},index=index)
df_model_v52 = pd.DataFrame({'MODEL_V52_PM25': MODEL_V52_PM25},index=index)
df_model_v54 = pd.DataFrame({'MODEL_V54_PM25': MODEL_V54_PM25},index=index)

def GetByIndex(state_name,urban_name,date_name):
    output_list1 = df_aqs.groupby(level='States').get_group(state_name).groupby(level='Urban').get_group(urban_name).groupby(level='Date').get_group(date_name)
    output_list2 = df_model_v52.groupby(level='States').get_group(state_name).groupby(level='Urban').get_group(urban_name).groupby(level='Date').get_group(date_name)
    output_list3 = df_model_v54.groupby(level='States').get_group(state_name).groupby(level='Urban').get_group(urban_name).groupby(level='Date').get_group(date_name)
    
    return output_list1, output_list2,output_list3

'''
3) get final data
'''
OBS_AQS___Virginia_urban_0718 = GetByIndex('Virginia','urban','7/18/2019')[0]
MODEL_v52_Virginia_urban_0718 = GetByIndex('Virginia','urban','7/18/2019')[1]
MODEL_v54_Virginia_urban_0718 = GetByIndex('Virginia','urban','7/18/2019')[2]

OBS_AQS___Virginia_urban_0719 = GetByIndex('Virginia','urban','7/19/2019')[0]
MODEL_v52_Virginia_urban_0719 = GetByIndex('Virginia','urban','7/19/2019')[1]
MODEL_v54_Virginia_urban_0719 = GetByIndex('Virginia','urban','7/19/2019')[2]

OBS_AQS___Virginia_rural_0718 = GetByIndex('Virginia','rural','7/18/2019')[0]
MODEL_v52_Virginia_rural_0718 = GetByIndex('Virginia','rural','7/18/2019')[1]
MODEL_v54_Virginia_rural_0718 = GetByIndex('Virginia','rural','7/18/2019')[2]

OBS_AQS___Virginia_rural_0719 = GetByIndex('Virginia','rural','7/19/2019')[0]
MODEL_v52_Virginia_rural_0719 = GetByIndex('Virginia','rural','7/19/2019')[1]
MODEL_v54_Virginia_rural_0719 = GetByIndex('Virginia','rural','7/19/2019')[2]


OBS_AQS___Massachusetts_urban_0718 = GetByIndex('Massachusetts','urban','7/18/2019')[0]
MODEL_v52_Massachusetts_urban_0718 = GetByIndex('Massachusetts','urban','7/18/2019')[1]
MODEL_v54_Massachusetts_urban_0718 = GetByIndex('Massachusetts','urban','7/18/2019')[2]

OBS_AQS___Massachusetts_urban_0719 = GetByIndex('Massachusetts','urban','7/19/2019')[0]
MODEL_v52_Massachusetts_urban_0719 = GetByIndex('Massachusetts','urban','7/19/2019')[1]
MODEL_v54_Massachusetts_urban_0719 = GetByIndex('Massachusetts','urban','7/19/2019')[2]

OBS_AQS___Massachusetts_rural_0718 = GetByIndex('Massachusetts','rural','7/18/2019')[0]
MODEL_v52_Massachusetts_rural_0718 = GetByIndex('Massachusetts','rural','7/18/2019')[1]
MODEL_v54_Massachusetts_rural_0718 = GetByIndex('Massachusetts','rural','7/18/2019')[2]

OBS_AQS___Massachusetts_rural_0719 = GetByIndex('Massachusetts','rural','7/19/2019')[0]
MODEL_v52_Massachusetts_rural_0719 = GetByIndex('Massachusetts','rural','7/19/2019')[1]
MODEL_v54_Massachusetts_rural_0719 = GetByIndex('Massachusetts','rural','7/19/2019')[2]


OBS_AQS___Texas_urban_0718 = GetByIndex('Texas','urban','7/18/2019')[0]
MODEL_v52_Texas_urban_0718 = GetByIndex('Texas','urban','7/18/2019')[1]
MODEL_v54_Texas_urban_0718 = GetByIndex('Texas','urban','7/18/2019')[2]

OBS_AQS___Texas_urban_0719 = GetByIndex('Texas','urban','7/19/2019')[0]
MODEL_v52_Texas_urban_0719 = GetByIndex('Texas','urban','7/19/2019')[1]
MODEL_v54_Texas_urban_0719 = GetByIndex('Texas','urban','7/19/2019')[2]

# OBS_AQS___Texas_rural_0718 = GetByIndex('Texas','rural','7/18/2019')[0]
# MODEL_v52_Texas_rural_0718 = GetByIndex('Texas','rural','7/18/2019')[1]
# MODEL_v54_Texas_rural_0718 = GetByIndex('Texas','rural','7/18/2019')[2]

# OBS_AQS___Texas_rural_0719 = GetByIndex('Texas','rural','7/19/2019')[0]
# MODEL_v52_Texas_rural_0719 = GetByIndex('Texas','rural','7/19/2019')[1]
# MODEL_v54_Texas_rural_0719 = GetByIndex('Texas','rural','7/19/2019')[2]

OBS_AQS___Iowa_urban_0718 = GetByIndex('Iowa','urban','7/18/2019')[0]
MODEL_v52_Iowa_urban_0718 = GetByIndex('Iowa','urban','7/18/2019')[1]
MODEL_v54_Iowa_urban_0718 = GetByIndex('Iowa','urban','7/18/2019')[2]

OBS_AQS___Iowa_urban_0719 = GetByIndex('Iowa','urban','7/19/2019')[0]
MODEL_v52_Iowa_urban_0719 = GetByIndex('Iowa','urban','7/19/2019')[1]
MODEL_v54_Iowa_urban_0719 = GetByIndex('Iowa','urban','7/19/2019')[2]

OBS_AQS___Iowa_rural_0718 = GetByIndex('Iowa','rural','7/18/2019')[0]
MODEL_v52_Iowa_rural_0718 = GetByIndex('Iowa','rural','7/18/2019')[1]
MODEL_v54_Iowa_rural_0718 = GetByIndex('Iowa','rural','7/18/2019')[2]

OBS_AQS___Iowa_rural_0719 = GetByIndex('Iowa','rural','7/19/2019')[0]
MODEL_v52_Iowa_rural_0719 = GetByIndex('Iowa','rural','7/19/2019')[1]
MODEL_v54_Iowa_rural_0719 = GetByIndex('Iowa','rural','7/19/2019')[2]


OBS_AQS___California_urban_0718 = GetByIndex('California','urban','7/18/2019')[0]
MODEL_v52_California_urban_0718 = GetByIndex('California','urban','7/18/2019')[1]
MODEL_v54_California_urban_0718 = GetByIndex('California','urban','7/18/2019')[2]

OBS_AQS___California_urban_0719 = GetByIndex('California','urban','7/19/2019')[0]
MODEL_v52_California_urban_0719 = GetByIndex('California','urban','7/19/2019')[1]
MODEL_v54_California_urban_0719 = GetByIndex('California','urban','7/19/2019')[2]

OBS_AQS___California_rural_0718 = GetByIndex('California','rural','7/18/2019')[0]
MODEL_v52_California_rural_0718 = GetByIndex('California','rural','7/18/2019')[1]
MODEL_v54_California_rural_0718 = GetByIndex('California','rural','7/18/2019')[2]

OBS_AQS___California_rural_0719 = GetByIndex('California','rural','7/19/2019')[0]
MODEL_v52_California_rural_0719 = GetByIndex('California','rural','7/19/2019')[1]
MODEL_v54_California_rural_0719 = GetByIndex('California','rural','7/19/2019')[2]


OBS_AQS___Wyoming_urban_0718 = GetByIndex('Wyoming','urban','7/18/2019')[0]
MODEL_v52_Wyoming_urban_0718 = GetByIndex('Wyoming','urban','7/18/2019')[1]
MODEL_v54_Wyoming_urban_0718 = GetByIndex('Wyoming','urban','7/18/2019')[2]

OBS_AQS___Wyoming_urban_0719 = GetByIndex('Wyoming','urban','7/19/2019')[0]
MODEL_v52_Wyoming_urban_0719 = GetByIndex('Wyoming','urban','7/19/2019')[1]
MODEL_v54_Wyoming_urban_0719 = GetByIndex('Wyoming','urban','7/19/2019')[2]

OBS_AQS___Wyoming_rural_0718 = GetByIndex('Wyoming','rural','7/18/2019')[0]
MODEL_v52_Wyoming_rural_0718 = GetByIndex('Wyoming','rural','7/18/2019')[1]
MODEL_v54_Wyoming_rural_0718 = GetByIndex('Wyoming','rural','7/18/2019')[2]

OBS_AQS___Wyoming_rural_0719 = GetByIndex('Wyoming','rural','7/19/2019')[0]
MODEL_v52_Wyoming_rural_0719 = GetByIndex('Wyoming','rural','7/19/2019')[1]
MODEL_v54_Wyoming_rural_0719 = GetByIndex('Wyoming','rural','7/19/2019')[2]




'''
4-1) calculate statistics RMSE
'''
import scipy 
from sklearn.metrics import mean_squared_error 
    

v1 = OBS_AQS___Wyoming_rural_0719
v2 = MODEL_v52_Wyoming_rural_0719
v3 = MODEL_v54_Wyoming_rural_0719

rms_test1 = mean_squared_error(v1,v2, squared=False)
rms_test2 = mean_squared_error(v1,v3, squared=False)

# print('rmse v52=',np.around(rms_test1,3))
# print('rmse v54=',np.around(rms_test2,3))


'''
4-2) calculate statistics Significant level
'''

X1=  np.array(MODEL_v52_Wyoming_rural_0719)
X2=  np.array(MODEL_v54_Wyoming_rural_0719)

#confidence interal 95% for CMAQ V5.2
mean_X1 = np.mean(X1)
STD_X1  = np.std(X1)
lower_bd_X1_95 = mean_X1 - 1.96*(STD_X1/(len(X1))**0.5)
upper_bd_X1_95 = mean_X1 + 1.96*(STD_X1/(len(X1))**0.5)

#confidence interal 95% for CMAQ V5.4
mean_X2 = np.mean(X2)
STD_X2  = np.std(X2)
lower_bd_X2_95 = mean_X2 - 1.96*(STD_X2/(len(X2))**0.5)
upper_bd_X2_95 = mean_X2 + 1.96*(STD_X2/(len(X2))**0.5)

#confidence interal 99% for CMAQ V5.2
lower_bd_X1_99 = mean_X1 - 2.576*(STD_X1/(len(X1))**0.5)
upper_bd_X1_99 = mean_X1 + 2.576*(STD_X1/(len(X1))**0.5)

#confidence interal 99% for CMAQ V5.4
lower_bd_X2_99 = mean_X2 - 2.576*(STD_X2/(len(X2))**0.5)
upper_bd_X2_99 = mean_X2 + 2.576*(STD_X2/(len(X2))**0.5)

#confidence interal 99.9% for CMAQ V5.2
lower_bd_X1_999 = mean_X1 - 3.291*(STD_X1/(len(X1))**0.5)
upper_bd_X1_999 = mean_X1 + 3.291*(STD_X1/(len(X1))**0.5)

#confidence interal 99.9% for CMAQ V5.4
lower_bd_X2_999 = mean_X2 - 3.291*(STD_X2/(len(X2))**0.5)
upper_bd_X2_999 = mean_X2 + 3.291*(STD_X2/(len(X2))**0.5)

print('cmaq v5.2',lower_bd_X1_95,upper_bd_X1_95)
print('cmaq v5.4',lower_bd_X2_95,upper_bd_X2_95)

if (upper_bd_X1_95 -lower_bd_X2_95)* (upper_bd_X2_95 -lower_bd_X1_95) >= 0:
    print('yes, overlap, No significant difference')
else:
    print('no, NOT overlap,signidicant difference')
    if (upper_bd_X1_99 -lower_bd_X2_99)* (upper_bd_X2_99 -lower_bd_X1_99) >= 0:
        print('95% confident')
    else:
        if (upper_bd_X1_999 -lower_bd_X2_999)* (upper_bd_X2_999 -lower_bd_X1_999) >= 0:
            print('99% confident')
        else:
            print('99.9% confident')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    