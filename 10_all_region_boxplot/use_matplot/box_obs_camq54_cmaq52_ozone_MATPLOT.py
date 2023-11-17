#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 13:28:17 2019

@author: tangbeiming
"""

import numpy as np
import pandas as pd
import xarray as xr
from matplotlib import pyplot as plt
import math


'''
0) initialization
'''
variable_name_obs = 'OZONE'  #CHANGE HERE 1
variable_name_cmaq52 = 'o3_ave'  #CHANGE HERE 2
variable_name_cmaq54 = 'o3_ave'   #CHANGE HERE 3

save_name = 'OZONE'                 #CHANGE HERE 4
'''
1) open dataset
'''
dir_ = './'                         #CHANGE HERE, folder of paired nc files
pattern1 = 'airnow_cmaq_v5p4_develop.nc4'    
ds1 = xr.open_dataset(dir_+pattern1)   

pattern2 = 'airnow_cmaq_v5p2.nc4'    
ds2 = xr.open_dataset(dir_+pattern2)   
'''
2) group by region
'''
ds1_new= ds1.groupby("epa_region")
R1_1 = ds1_new['R1']
R2_1 = ds1_new['R2']
R3_1 = ds1_new['R3']
R4_1 = ds1_new['R4']
R5_1 = ds1_new['R5']
R6_1 = ds1_new['R6']
R7_1 = ds1_new['R7']
R8_1 = ds1_new['R8']
R9_1 = ds1_new['R9']
R10_1 = ds1_new['R10']

ds2_new= ds2.groupby("epa_region")
R1_2 = ds2_new['R1']
R2_2 = ds2_new['R2']
R3_2 = ds2_new['R3']
R4_2 = ds2_new['R4']
R5_2 = ds2_new['R5']
R6_2 = ds2_new['R6']
R7_2 = ds2_new['R7']
R8_2 = ds2_new['R8']
R9_2 = ds2_new['R9']
R10_2 = ds2_new['R10']

R1_V_OBS_1 = R1_1[variable_name_obs]
R1_V_CMAQ54 = R1_1[variable_name_cmaq54]
R2_V_OBS_1 = R2_1[variable_name_obs]
R2_V_CMAQ54 = R2_1[variable_name_cmaq54]
R3_V_OBS_1 = R3_1[variable_name_obs]
R3_V_CMAQ54 = R3_1[variable_name_cmaq54]
R4_V_OBS_1 = R4_1[variable_name_obs]
R4_V_CMAQ54 = R4_1[variable_name_cmaq54]
R5_V_OBS_1 = R5_1[variable_name_obs]
R5_V_CMAQ54 = R5_1[variable_name_cmaq54]
R6_V_OBS_1 = R6_1[variable_name_obs]
R6_V_CMAQ54 = R6_1[variable_name_cmaq54]
R7_V_OBS_1 = R7_1[variable_name_obs]
R7_V_CMAQ54 = R7_1[variable_name_cmaq54]
R8_V_OBS_1 = R8_1[variable_name_obs]
R8_V_CMAQ54 = R8_1[variable_name_cmaq54]
R9_V_OBS_1 = R9_1[variable_name_obs]
R9_V_CMAQ54 = R9_1[variable_name_cmaq54]
R10_V_OBS_1 = R10_1[variable_name_obs]
R10_V_CMAQ54 = R10_1[variable_name_cmaq54]

R1_V_OBS_2 = R1_2[variable_name_obs]
R1_V_CMAQ52 = R1_2[variable_name_cmaq54]
R2_V_OBS_2 = R2_2[variable_name_obs]
R2_V_CMAQ52 = R2_2[variable_name_cmaq54]
R3_V_OBS_2 = R3_2[variable_name_obs]
R3_V_CMAQ52 = R3_2[variable_name_cmaq54]
R4_V_OBS_2 = R4_2[variable_name_obs]
R4_V_CMAQ52 = R4_2[variable_name_cmaq54]
R5_V_OBS_2 = R5_2[variable_name_obs]
R5_V_CMAQ52 = R5_2[variable_name_cmaq54]
R6_V_OBS_2 = R6_2[variable_name_obs]
R6_V_CMAQ52 = R6_2[variable_name_cmaq54]
R7_V_OBS_2 = R7_2[variable_name_obs]
R7_V_CMAQ52 = R7_2[variable_name_cmaq54]
R8_V_OBS_2 = R8_2[variable_name_obs]
R8_V_CMAQ52 = R8_2[variable_name_cmaq54]
R9_V_OBS_2 = R9_2[variable_name_obs]
R9_V_CMAQ52 = R9_2[variable_name_cmaq54]
R10_V_OBS_2 = R10_2[variable_name_obs]
R10_V_CMAQ52 = R10_2[variable_name_cmaq54]


'''
3) kick out Nan Values 
'''
def GetPair(obs_input,model_input):
    len_time = len(obs_input)
    len_site = len(obs_input[0])
    
    obs_reshape = np.array(obs_input).reshape((1,len_time*len_site))
    model_reshape = np.array(model_input).reshape((1,len_time*len_site))
    
    obs_output = []
    model_output = []
    for i in range(len(obs_reshape[0])):
        if math.isnan(float(obs_reshape[0][i])) == False:
            if math.isnan(float(model_reshape[0][i])) == False:
                obs_output.append(obs_reshape[0][i])
                model_output.append(model_reshape[0][i])
    
    return obs_output, model_output

obs_output_r1, model_54_output_r1 = GetPair(R1_V_OBS_1 , R1_V_CMAQ54)
obs_output_r2, model_54_output_r2 = GetPair(R2_V_OBS_1 , R2_V_CMAQ54)
obs_output_r3, model_54_output_r3 = GetPair(R3_V_OBS_1 , R3_V_CMAQ54)
obs_output_r4, model_54_output_r4 = GetPair(R4_V_OBS_1 , R4_V_CMAQ54)
obs_output_r5, model_54_output_r5 = GetPair(R5_V_OBS_1 , R5_V_CMAQ54)
obs_output_r6, model_54_output_r6 = GetPair(R6_V_OBS_1 , R6_V_CMAQ54)
obs_output_r7, model_54_output_r7 = GetPair(R7_V_OBS_1 , R7_V_CMAQ54)
obs_output_r8, model_54_output_r8 = GetPair(R8_V_OBS_1 , R8_V_CMAQ54)
obs_output_r9, model_54_output_r9 = GetPair(R9_V_OBS_1 , R9_V_CMAQ54)
obs_output_r10, model_54_output_r10 = GetPair(R10_V_OBS_1 , R10_V_CMAQ54)

obs_output_r1_, model_52_output_r1 = GetPair(R1_V_OBS_2 , R1_V_CMAQ52)
obs_output_r2_, model_52_output_r2 = GetPair(R2_V_OBS_2 , R2_V_CMAQ52)
obs_output_r3_, model_52_output_r3 = GetPair(R3_V_OBS_2 , R3_V_CMAQ52)
obs_output_r4_, model_52_output_r4 = GetPair(R4_V_OBS_2 , R4_V_CMAQ52)
obs_output_r5_, model_52_output_r5 = GetPair(R5_V_OBS_2 , R5_V_CMAQ52)
obs_output_r6_, model_52_output_r6 = GetPair(R6_V_OBS_2 , R6_V_CMAQ52)
obs_output_r7_, model_52_output_r7 = GetPair(R7_V_OBS_2 , R7_V_CMAQ52)
obs_output_r8_, model_52_output_r8 = GetPair(R8_V_OBS_2 , R8_V_CMAQ52)
obs_output_r9_, model_52_output_r9 = GetPair(R9_V_OBS_2 , R9_V_CMAQ52)
obs_output_r10_, model_52_output_r10 = GetPair(R10_V_OBS_2 , R10_V_CMAQ52)


'''
4) box plot
'''

'''
4-2) USE MATPLOT
'''
fig = plt.subplots(1,1, figsize = (20,10))  
plt.rc('ytick', labelsize=30)
plt.rc('xtick', labelsize=30)

labels = ['','R1','','','R2','','','R3','','','R4','','','R5','',
          '','R6','','','R7','','','R8','','','R9','','','R10','']


bplot = plt.boxplot([obs_output_r1, model_54_output_r1,model_52_output_r1,
                     obs_output_r2, model_54_output_r2,model_52_output_r2,
                     obs_output_r3, model_54_output_r3,model_52_output_r3,
                     obs_output_r4, model_54_output_r4,model_52_output_r4,
                     obs_output_r5, model_54_output_r5,model_52_output_r5,
                     obs_output_r6, model_54_output_r6,model_52_output_r6,
                     obs_output_r7, model_54_output_r7,model_52_output_r7,
                     obs_output_r8, model_54_output_r8,model_52_output_r8,
                     obs_output_r9, model_54_output_r9,model_52_output_r9,
                     obs_output_r10, model_54_output_r10,model_52_output_r10],
                     vert = True, widths = 0.2, 
                     positions = [0.8,1,1.2,
                                  1.8,2,2.2,
                                  2.8,3,3.2,
                                  3.8,4,4.2,
                                  4.8,5,5.2,
                                  5.8,6,6.2,
                                  6.8,7,7.2,
                                  7.8,8,8.2,
                                  8.8,9,9.2,
                                  9.8,10,10.2], 
                     patch_artist = True,whiskerprops=dict(linestyle='dashed'),labels = labels, zorder=0,
                     showfliers=False)

colors = ['gray','blue','red','gray','blue','red','gray','blue','red','gray','blue','red','gray','blue','red',
          'gray','blue','red','gray','blue','red','gray','blue','red','gray','blue','red','gray','blue','red']
for patch,median,color in zip(bplot['boxes'],bplot['medians'],colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('k')
    median.set_color('k')

plt.text(0.5,52,'Airnow',color='gray',fontsize=30,fontweight="bold")
plt.text(0.5,49,'CMAQ v5.4',color='blue',fontsize=30,fontweight="bold")
plt.text(0.5,46,'CMAQ v5.2',color='red',fontsize=30,fontweight="bold")

plt.ylim(15,55)  #CHANGE HERE 5
plt.ylabel('O$_3$ \n(ppbv)',fontsize = 30)  #CHANGE HERE 6

plt.savefig('boxplot_'+save_name+'.png', dpi=600)


