#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 13:28:17 2019

@author: tangbeiming
"""

import numpy as np
import pandas as pd
import xarray as xr

import matplotlib.pyplot as plt

'''
0) initialization
'''
cmaq54_name = 'co'
cmaq52_name = 'co'
obs_name = 'CO'

save_name = 'CO'
vmin = 100
vmax = 550


'''
1) open dataset
'''
dir_ = '/Volumes/Ext_Disk_1/3_NOAA_projects/NOAA_cmaq_project/CODE/10_all_regions_box_plot/'  #location of paired netcdf files
pattern1 = 'airnow_cmaq_v5p4_develop.nc4'    
ds1 = xr.open_dataset(dir_+pattern1)   

pattern2 = 'airnow_cmaq_v5p2.nc4'    
ds2 = xr.open_dataset(dir_+pattern2)  


pm25_cmaq54 =ds1[cmaq54_name].to_dataframe().rename({cmaq54_name:obs_name},axis=1)
pm25_obs =ds1[obs_name].to_dataframe().rename({obs_name:obs_name},axis=1)  
pm25_cmaq52 =ds2[cmaq54_name].to_dataframe().rename({cmaq54_name:obs_name},axis=1)

'''
2) create a region column
'''
regions = ds1['epa_region'].to_dataframe()
regions_new = []
for i in range(int(len(pm25_obs)/len(regions))):
    # print(i)
    for j in range(len(regions)):
        regions_new.append(regions['epa_region'][j])


'''
3) add 2 columns for the dataset
'''
pm25_cmaq54['model'] = 'CMAQv54'  
pm25_obs['model'] = 'AirNow'
pm25_cmaq52['model'] = 'CMAQv52'

pm25_cmaq54['Regions'] = regions_new
pm25_obs['Regions'] = regions_new
pm25_cmaq52['Regions'] = regions_new

'''
4) combine the output dataset
'''
tdf =pd.concat([pm25_obs[[obs_name,'model','Regions']],pm25_cmaq54[[obs_name,'model','Regions']],pm25_cmaq52[[obs_name,'model','Regions']]])
acro = ['R1','R2','R3','R4','R5','R6','R7','R8','R9','R10']

'''
2) Boxplot using SEABORN
'''
import seaborn as sns
fig,ax = plt.subplots(1,1, figsize = (20,10))  
plt.rc('ytick', labelsize=30)
plt.rc('xtick', labelsize=30)


ax= sns.boxplot(x='Regions',y=obs_name,hue='model',
                data=tdf.loc[tdf.Regions.isin(acro)], order = acro, showfliers=False)
plt.ylim(vmin,vmax)
ax.set_ylabel(save_name,fontsize=30)
ax.set_xlabel('Regions', fontsize=30)
plt.legend(fontsize = 30,loc='upper right')
plt.savefig('syn_boxplot_'+save_name+'.png', dpi=600)




