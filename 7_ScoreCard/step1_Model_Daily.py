#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 17:07:08 2022

@author: btang1
"""

import numpy as np
import os
from scipy import spatial
import fnmatch
from netCDF4 import Dataset
import codecs
import datetime
from datetime import datetime as dt


'''
1) read in model 1 & 2 hourly data
'''
dir_ = '/Volumes/Ext_Disk_1/3_NOAA_projects/NOAA_cmaq_project/beiming_code/score_card/'

pattern_1 = 'Surface_Map_pm25_v52.nc'
filename_1 = dir_ + pattern_1
f1 = Dataset(filename_1,'r')
LAT = f1.variables['lat'][:] #(225,393)
LON = f1.variables['lon'][:] #(225,393)
pm25_v52 = f1.variables['pm25'][:][1:]  #(49,225,393) --> (48,225,393)

pattern_2 = 'Surface_Map_pm25_v54.nc'
filename_2 = dir_ + pattern_2
f2 = Dataset(filename_2,'r')
pm25_v54 = f2.variables['pm25'][:][1:] 

pattern_3 = 'Surface_Map_o3_v52.nc'
filename_3 = dir_ + pattern_3
f3 = Dataset(filename_3,'r')
o3_v52 = f3.variables['o3'][:][1:]

pattern_4 = 'Surface_Map_o3_v54.nc'
filename_4 = dir_ + pattern_4
f4 = Dataset(filename_4,'r')
o3_v54 = f4.variables['o3'][:][1:]

lat_index = int(np.shape(LAT)[1]/2)
LAT_MODEL = np.transpose(LAT)[lat_index]

lon_index = int(np.shape(LON)[0]/2)
LON_MODEL = LON[lon_index]

'''
2) get daily model data
'''
def ModelDaily(input_matrix):
    AAA = []
    aaa = np.zeros((np.shape(LAT)[0],np.shape(LAT)[1]))
    for i in range(len(input_matrix)):
        if i% 24 == 23:
            aaa = aaa + input_matrix[i]
            aaa = aaa/24
            AAA.append(aaa)
            aaa = np.zeros((np.shape(LAT)[0],np.shape(LAT)[1]))
            
        else:
            aaa = aaa + input_matrix[i]
            
    return AAA

pm25_v52_daily = ModelDaily(pm25_v52)
pm25_v54_daily = ModelDaily(pm25_v54)
o3_v52_daily = ModelDaily(o3_v52)
o3_v54_daily = ModelDaily(o3_v54)








    
    
    
    






    
    
    
    
    
    
    
    
    
    
    