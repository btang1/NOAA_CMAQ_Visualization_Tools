#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 13:28:17 2019

@author: tangbeiming
"""

import numpy as np
# import pandas as pd
import xarray as xr
from matplotlib import pyplot as plt
import math
from sklearn.metrics import mean_squared_error 

'''
0) initialization
'''
variable_name_obs = 'NO2'
variable_name_cmaq54 = 'no2_ave'
variable_name_cmaq52 = 'no2_ave'

save_name = 'NO2'
'''
1) open dataset
'''
dir_ = '/Volumes/Ext_Disk_1/3_NOAA_projects/NOAA_cmaq_project/CODE/9_score_card/'
pattern1 = 'airnow_cmaq_v5p4_develop.nc4'    
ds1 = xr.open_dataset(dir_+pattern1)   

pattern2 = 'airnow_cmaq_v5p2.nc4'    
ds2 = xr.open_dataset(dir_+pattern2)   
 
'''
2) group by region
'''
ds1_new= ds1.groupby("epa_region")
ds2_new= ds2.groupby("epa_region")

'''
2-2)to get (region & time)
'''

date_list = ['2023-08-01','2023-08-02','2023-08-03','2023-08-04','2023-08-05',
              '2023-08-06','2023-08-07','2023-08-08','2023-08-09','2023-08-10',
              '2023-08-11','2023-08-12','2023-08-13','2023-08-14','2023-08-15',
              '2023-08-16','2023-08-17','2023-08-18','2023-08-19','2023-08-20',
              '2023-08-21','2023-08-22','2023-08-23','2023-08-24','2023-08-25',
              '2023-08-26','2023-08-27','2023-08-28','2023-08-29','2023-08-30']

region_list = ['R1','R2','R3','R4','R5',
               'R6','R7','R8','R9','R10']


def GetLUC(region_name_input,ds_name):
    msa_here = ds_name[region_name_input]['msa_name']
    msa_here_array = np.array(msa_here).reshape((1,len(msa_here)))
    rural_index_list = []
    urban_index_list = []
    for i in range(len(msa_here_array[0])):
        if msa_here_array[0][i] == '':
            rural_index_list.append(i)
        else:
            urban_index_list.append(i)
    return rural_index_list, urban_index_list
        
    
    
def GetRegionLUCDate(variable_name,ds_name):
    Region_Date_Urban_list = [] #(region * date)
    Region_Date_Rural_list = [] #(region * date)
    
    for region in region_list:
        region_here = ds_name[region] #ds1_new['R1'] ~(2162,85)
            
        Date_Urban_List = []
        Date_Rural_List = []
        
        for date in date_list:
            date_region_here = region_here[variable_name].loc[date,:] #ds1_new['R1']['PM2.5'].loc['2023-08-01',:]  ~ (72,85)
            
            rural_index_list_here = GetLUC(region,ds_name)[0]
            # urban_index_list_here = GetLUC(region,ds_name)[1]
            
            date_region_rural_here = []
            date_region_urban_here = []
            for i in range(len(date_region_here[0])): #85
                if i in rural_index_list_here:
                    date_region_rural_here.append(date_region_here[:,i])
                else:
                    date_region_urban_here.append(date_region_here[:,i])
                    
                
            
            date_region_rural_here_array = np.array(date_region_rural_here).reshape((1,len(date_region_rural_here)*len(date_region_rural_here[0])))    
            date_region_urban_here_array = np.array(date_region_urban_here).reshape((1,len(date_region_urban_here)*len(date_region_urban_here[0])))    
            
            
            Date_Urban_List.append(date_region_urban_here_array)  # all date pm2.5
            Date_Rural_List.append(date_region_rural_here_array)  # all date pm2.5
            
            
        Region_Date_Urban_list.append(Date_Urban_List) # all region & data pm2.5
        Region_Date_Rural_list.append(Date_Rural_List) # all region & data pm2.5
        
    return Region_Date_Urban_list, Region_Date_Rural_list

OBS_Region_Date_Urban_list, OBS_Region_Date_Rural_list,= GetRegionLUCDate(variable_name_obs ,ds1_new)             #AirNow
MODEL_54_Region_Date_Urban_list, MODEL_54_Region_Date_Rural_list= GetRegionLUCDate(variable_name_cmaq54,ds1_new)  #cmaq v5.4
MODEL_52_Region_Date_Urban_list, MODEL_52_Region_Date_Rural_list= GetRegionLUCDate(variable_name_cmaq52,ds2_new)  #cmaq v5.4


'''
3) kick out Nan values
'''
def KickNan(obs_input, model_input_1, model_input_2): #ORDER: (airnow, cmaq52, cmaq54)
    OBS_Region_Date_list_noNan = []
    MODEL_54_Region_Date_list_noNan = [] #(region, date)
    MODEL_52_Region_Date_list_noNan = []
    for kk in range(len(obs_input)):
        OBS_Region_Date_list_noNan_Date = []
        MODEL_54_Region_Date_list_noNan_Date = []
        MODEL_52_Region_Date_list_noNan_Date = []
        
        for jj in range(len(obs_input[kk])):
            obs_here_array = obs_input[kk][jj]
            model_54_here_array = model_input_2[kk][jj]
            model_52_here_array = model_input_1[kk][jj]
            
            obs_output = []
            model_54_output = []
            model_52_output = []
            for i in range(len(obs_here_array[0])):
                if math.isnan(float(obs_here_array[0][i])) == False:
                    if math.isnan(float(model_54_here_array[0][i])) == False:
                        obs_output.append(obs_here_array[0][i])
                        model_54_output.append(model_54_here_array[0][i])
                        model_52_output.append(model_52_here_array[0][i])
                        
            OBS_Region_Date_list_noNan_Date.append(obs_output)
            MODEL_54_Region_Date_list_noNan_Date.append(model_54_output)
            MODEL_52_Region_Date_list_noNan_Date.append(model_52_output)
        OBS_Region_Date_list_noNan.append(OBS_Region_Date_list_noNan_Date)
        MODEL_54_Region_Date_list_noNan.append(MODEL_54_Region_Date_list_noNan_Date)
        MODEL_52_Region_Date_list_noNan.append(MODEL_52_Region_Date_list_noNan_Date)
        
    return OBS_Region_Date_list_noNan,MODEL_52_Region_Date_list_noNan,MODEL_54_Region_Date_list_noNan
                    
OBS_Region_Date_Urban_list_noNan,MODEL_52_Region_Date_Urban_list_noNan,MODEL_54_Region_Date_Urban_list_noNan = KickNan(OBS_Region_Date_Urban_list,
                                                                                                               MODEL_52_Region_Date_Urban_list,
                                                                                                               MODEL_54_Region_Date_Urban_list)    
            
OBS_Region_Date_Rural_list_noNan,MODEL_52_Region_Date_Rural_list_noNan,MODEL_54_Region_Date_Rural_list_noNan = KickNan(OBS_Region_Date_Rural_list,
                                                                                                               MODEL_52_Region_Date_Rural_list,
                                                                                                               MODEL_54_Region_Date_Rural_list)                 
'''
4) calculate statistics
'''
'''
4-1) Use RMSE to determinet better or worse
'''

def BW(obs_input,model_1_input, model_2_input):  #ORDER: airnow, cmaq_52, cmaq_54
    v1 = obs_input
    v2 = model_1_input
    v3 = model_2_input
    
    key_word = ''
    rms_test1 = mean_squared_error(v1,v2, squared=False)
    rms_test2 = mean_squared_error(v1,v3, squared=False)
    
    if rms_test1 < rms_test2:
        key_word= 'worse'
    elif rms_test1 > rms_test2:
        key_word = 'better'
    else:
        key_word = 'equal'
        
    return key_word

'''
4-2) calcualte Significant level
'''
def SigLevel(model_input_1,model_input_2):  #ORDER: cmaq_52, cmaq_54
    X1=  np.array(model_input_1)
    X2=  np.array(model_input_2)
    
    #confidence interal 95% for model 1
    mean_X1 = np.mean(X1)
    STD_X1  = np.std(X1)
    lower_bd_X1_95 = mean_X1 - 1.96*(STD_X1/(len(X1))**0.5)
    upper_bd_X1_95 = mean_X1 + 1.96*(STD_X1/(len(X1))**0.5)
    
    #confidence interal 95% for model 2
    mean_X2 = np.mean(X2)
    STD_X2  = np.std(X2)
    lower_bd_X2_95 = mean_X2 - 1.96*(STD_X2/(len(X2))**0.5)
    upper_bd_X2_95 = mean_X2 + 1.96*(STD_X2/(len(X2))**0.5)
    
    #confidence interal 99% for model 1
    lower_bd_X1_99 = mean_X1 - 2.576*(STD_X1/(len(X1))**0.5)
    upper_bd_X1_99 = mean_X1 + 2.576*(STD_X1/(len(X1))**0.5)
    
    #confidence interal 99% for model 2
    lower_bd_X2_99 = mean_X2 - 2.576*(STD_X2/(len(X2))**0.5)
    upper_bd_X2_99 = mean_X2 + 2.576*(STD_X2/(len(X2))**0.5)
    
    #confidence interal 99.9% for model 1
    lower_bd_X1_999 = mean_X1 - 3.291*(STD_X1/(len(X1))**0.5)
    upper_bd_X1_999 = mean_X1 + 3.291*(STD_X1/(len(X1))**0.5)
    
    #confidence interal 99.9% for model 2
    lower_bd_X2_999 = mean_X2 - 3.291*(STD_X2/(len(X2))**0.5)
    upper_bd_X2_999 = mean_X2 + 3.291*(STD_X2/(len(X2))**0.5)
    
    key_word = ''
    
    if (upper_bd_X1_95 -lower_bd_X2_95)* (upper_bd_X2_95 -lower_bd_X1_95) >= 0:
        key_word = 'No significant difference'
    else: #NOT overlap,signidicant difference'
        if (upper_bd_X1_99 -lower_bd_X2_99)* (upper_bd_X2_99 -lower_bd_X1_99) >= 0:
            key_word = 'significant difference, with 95% confident'
        else:
            if (upper_bd_X1_999 -lower_bd_X2_999)* (upper_bd_X2_999 -lower_bd_X1_999) >= 0:
                key_word = 'significant difference, with 99% confident'
            else:
                key_word = 'significant difference, with 99.9% confident'
                
    return key_word
'''
4-3) for each grid-cell in table, use 4-1 & 4-2 to fill
'''

output_matrix = np.zeros((len(OBS_Region_Date_Urban_list_noNan)+len(OBS_Region_Date_Rural_list_noNan),len(OBS_Region_Date_Urban_list_noNan[0])))  #(region, date)

for i in range(len(OBS_Region_Date_Urban_list_noNan)+len(OBS_Region_Date_Rural_list_noNan)):# i is region
    for j in range(len(OBS_Region_Date_Urban_list_noNan[0])):# j is date
        if i%2 == 0: # this is urban
            cmaq52_here = MODEL_52_Region_Date_Urban_list_noNan[int(i/2)][j]
            cmaq54_here = MODEL_54_Region_Date_Urban_list_noNan[int(i/2)][j]
            OBS_here = OBS_Region_Date_Urban_list_noNan[int(i/2)][j]
        else:   # this is rural
            cmaq52_here = MODEL_52_Region_Date_Rural_list_noNan[int((i-1)/2)][j]
            cmaq54_here = MODEL_54_Region_Date_Rural_list_noNan[int((i-1)/2)][j]
            OBS_here = OBS_Region_Date_Rural_list_noNan[int((i-1)/2)][j]
        
        if OBS_here == []:
            output_matrix[i][j] = np.nan  # no values, need to change
        else:
            key_word_BW = BW(OBS_here,cmaq52_here, cmaq54_here)  #ORDER: airnow, cmaq_52, cmaq_54
            key_word_SL = SigLevel(cmaq52_here, cmaq54_here)     #ORDER: cmaq_52, cmaq_54
            
            if key_word_SL == 'No significant difference':
                output_matrix[i][j] = 0   #'no significant difference'
                
            elif key_word_SL == 'significant difference, with 95% confident':
                if key_word_BW == 'better':
                    output_matrix[i][j] = 20  #'95% better'
                elif key_word_BW == 'worse':
                    output_matrix[i][j] = -20 #'95% worse'
                else:
                    output_matrix[i][j] = 0  #'95% equal'
                    
            elif key_word_SL == 'significant difference, with 99% confident':
                if key_word_BW == 'better':
                    output_matrix[i][j] = 50  #'99% better'
                elif key_word_BW == 'worse':
                    output_matrix[i][j] = -50 #'99% worse'
                else:
                    output_matrix[i][j] = 0  #'99% equal'
                    
            else:
                if key_word_BW == 'better':
                    output_matrix[i][j] = 100  #'99.9% better'
                elif key_word_BW == 'worse':
                    output_matrix[i][j] = -100 #'99.9% worse'
                else:
                    output_matrix[i][j] = 0   #'99.9% equal'     

'''
5) ploting
'''
fig, ax = plt.subplots(figsize=(18,10))

ax.set_title('NO$_2$ CMAQv5.4 vs. v5.2 Evaluated against AirNow OBS \n based on RMSE & Signigicant Level',fontsize = 30)
# ax.set_xlabel('Date',fontsize = 30)
ax.set_ylabel('Regions',fontsize = 30)

'''
5-2) set ticks
'''
ax.tick_params(labelsize = 20)

x_labels = ['08/01','08/06','08/11','08/16','08/21','08/26','08/30']
ax.set_xticks([0.5,5.5,10.5,15.5,20.5,25.5,29.5],
            x_labels,rotation=0)  

y_labels =  region_list   
ax.set_yticks([1,3,5,7,9,11,13,15,17,19],
            y_labels)    
      
plt.gca().invert_yaxis()  #to verse Y axis 

'''
5-2-2) add another y-axis
'''
ax2=ax.secondary_yaxis('right')
ax2.tick_params(labelsize = 20)
y2_labels =[]
for i in range(len(region_list)):
    y2_labels.append('urban')
    y2_labels.append('rural')
ax2.set_yticks([i+0.5 for i in range(len(region_list)*2)],
            y2_labels)  
'''
5-3) set colorbar
'''
plot1= plt.pcolormesh(output_matrix,cmap='cividis',edgecolor='k',vmin=-100,vmax=100) #colorblind frindly
# plot1= plt.pcolormesh(output_matrix,cmap='coolwarm',edgecolor='k',vmin=-100,vmax=100)


cb = fig.colorbar(plot1,ticks=[-100,-50,-20,0,20,50,100],pad=0.1)
cb.ax.set_yticklabels(['99.9% Worse','99% Worse','95% Worse',
                  'No Significant Difference',
                  '95% Better','99% Better','99.9% Better'])
cb.ax.tick_params(labelsize = 20)

'''
5-4) save figure
'''
plt.savefig('ScoreCard_LUC2_'+save_name+'.png', dpi=600)













