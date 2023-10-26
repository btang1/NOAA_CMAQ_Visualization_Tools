#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 15:49:54 2022

@author: btang1
"""


import numpy as np
# import os
# from scipy import spatial
import fnmatch
from netCDF4 import Dataset
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from mpl_toolkits.basemap import Basemap
import codecs
import datetime
from datetime import datetime as dt
# import h5py
import pandas as pd
import statistics as stat


'''
1) import data
'''
from step1_Model_Daily import LAT_MODEL, LON_MODEL,pm25_v52_daily,pm25_v54_daily,o3_v52_daily,o3_v54_daily
from step2_AQS_Daily_PM25 import LOC_NUMBER_OBS_FINAL, PM_OBS_FINAL, TIME_OBS_FINAL,LAT_OBS_FINAL,LON_OBS_FINAL,LUC_OBS_FINAL,STATE_OBS_FINAL
from step2_AQS_Daily_PM25 import campaign_start_time
   
        
'''
2) define model
'''

def GetInterpolate(time_input,lon_input,lat_input, variable_input):
    
    lat_obs = lat_input
    lon_obs = lon_input
    
    lat_model  = LAT_MODEL #225
    lon_model  = LON_MODEL #393
    variable_model = variable_input  # (30,2500,3500)                                       
    
    c = 'no_value'
    for i in range(1,len(lat_model)):           #225
        if (lat_model[i-1]-lat_obs)*(lat_model[i]-lat_obs) < 0: 
            
            for j in range(1,len(lon_model)):   #393 
                if (lon_model[j-1]-lon_obs)*(lon_model[j]-lon_obs) < 0:     
                    
                    x1 = np.abs((lon_model[j-1]-lon_obs)/(lon_model[j-1]-lon_model[j]))
                    x2 = np.abs((lon_model[j]-lon_obs)/(lon_model[j-1]-lon_model[j]))
                    
                    y1 = np.abs((lat_model[i-1]-lat_obs)/(lat_model[i-1]-lat_model[i]))
                    y2 = np.abs((lat_model[i]-lat_obs)/(lat_model[i-1]-lat_model[i]))
                    
                    for k in range(len(variable_input)):  #days of surface map pm2.5
                        if time_input.day - campaign_start_time.day == k+1:
                            a = x2 * variable_model[k][i-1][j-1] + x1 * variable_model[k][i-1][j]
                            b = x2 * variable_model[k][i][j-1] + x1 * variable_model[k][i][j]
                            c = y1 * b + y2 * a  
                            break
                    break
            break
            
    return c
'''
3) 2d-interpolation MAIN
'''
V1 = pm25_v52_daily
V2 = pm25_v54_daily

V1_final_list = []   
V2_final_list = []   
 
for i in range(len(TIME_OBS_FINAL)):             
  
    loc_number_here = LOC_NUMBER_OBS_FINAL[i]
    lat_here = LAT_OBS_FINAL[i]
    lon_here = LON_OBS_FINAL[i]

    V1_final =  GetInterpolate(TIME_OBS_FINAL[i],lon_here,lat_here, V1)
    V2_final =  GetInterpolate(TIME_OBS_FINAL[i],lon_here,lat_here, V2)    
    
    print(i,TIME_OBS_FINAL[i],lon_here,lat_here,V1_final)
    
    V1_final_list.append(V1_final)
    V2_final_list.append(V2_final)

'''
4) convert land use cover
'''
urban_list = ['COMMERCIAL','INDUSTRIAL','MILITARY RESERVATION','RESIDENTIAL']
rural_list = ['AGRICULTURAL','DESERT','FOREST','MOBILE','UNKNOWN']
Urban_obs_Final = []
for i in range(len(LUC_OBS_FINAL) ):
    if LUC_OBS_FINAL[i] in urban_list:
        Urban_obs_Final.append('urban')
    else:
        Urban_obs_Final.append('rural')
        
'''
3) write output into excel
'''
from xlwt import Workbook


wb = Workbook()
sheet1 = wb.add_sheet('EPA_AQS_pm25')

sheet1.write(0,0,'no')
sheet1.write(0,1,'Date')
sheet1.write(0,2,'Location_number')
sheet1.write(0,3,'AQS_OBS_PM25')
sheet1.write(0,4,'MODEL_V52_PM25')
sheet1.write(0,5,'MODEL_V54_PM25')
sheet1.write(0,6,'STATES')
sheet1.write(0,7,'LAND_USE_COVER')
sheet1.write(0,8,'URBAN')

for i in range(len(V1_final_list)):  
    sheet1.write(i+1,0,int(i+1))
    sheet1.write(i+1,1,str(TIME_OBS_FINAL[i].month)+'/'+str(TIME_OBS_FINAL[i].day)+'/'+str(TIME_OBS_FINAL[i].year))
    sheet1.write(i+1,2,LOC_NUMBER_OBS_FINAL[i])
    sheet1.write(i+1,3,PM_OBS_FINAL[i])    
    sheet1.write(i+1,4,V1_final_list[i])
    sheet1.write(i+1,5,V2_final_list[i])
    sheet1.write(i+1,6,STATE_OBS_FINAL[i]) 
    sheet1.write(i+1,7,LUC_OBS_FINAL[i]) 
    sheet1.write(i+1,8,Urban_obs_Final[i]) 


    
wb.save('US_interpolated_AQS_PM25.xls')
    
            
            
        





























