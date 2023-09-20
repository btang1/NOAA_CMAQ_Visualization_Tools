#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 17:17:41 2020

@author: beimingtao
"""

import numpy as np
import os
import scipy
from scipy import spatial
import fnmatch
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.basemap import Basemap
import codecs
import datetime
from datetime import datetime as dt

'''
1) import gs data
'''
# dir_gs = '/Users/beimingtao/Desktop/Data/gs_data/gs_Olympic_park/' 
# pattern_gs = 'korusaq-O3-BC-PM_GROUND-NIER-OLYMPIC-PARK_20160508_RA.ict'  
# filename_gs = dir_gs+pattern_gs
# with codecs.open(filename_gs,"r",encoding='utf-8', errors='ignore') as fdata:
#     lines = fdata.readlines()

# v = lines[41].replace(' ','')   #change 5
# v_olympic_park = v.split(',')

# data_olympic_park = []
# for line in lines[42:]:          #change 6
#     line = line.split(',')
#     data_olympic_park.append(line) 

# Time_o3_gs = []
# O3_gs = []

# Time_bc_gs = []
# Bc_gs = []

# Time_oc_gs = []
# Oc_gs = []

# Time_pm25_gs = []
# Pm25_gs = []

# Time_pm10_gs = []
# Pm10_gs = []

# for ii in range(len(data_olympic_park)):
    
#     time_gs = str(int(data_olympic_park[ii][3]))   
#     date_object = dt.strptime(time_gs, '%Y%m%d%H%M%S')
    
#     o3_gs = float(data_olympic_park[ii][4])     
#     if o3_gs >= 0:
#         O3_gs.append(o3_gs)
#         Time_o3_gs.append(date_object)

#     bc_gs = float(data_olympic_park[ii][7])     
#     if bc_gs >= 0:
#         Bc_gs.append(bc_gs/1000)
#         Time_bc_gs.append(date_object)

#     oc_gs = float(data_olympic_park[ii][8])  
#     if oc_gs >= 0:
#         Oc_gs.append(oc_gs/1000)
#         Time_oc_gs.append(date_object)        

#     pm25_gs = float(data_olympic_park[ii][10])  
#     if pm25_gs >= 0:
#         Pm25_gs.append(pm25_gs)
#         Time_pm25_gs.append(date_object) 

#     pm10_gs = float(data_olympic_park[ii][9])  
#     if pm10_gs >= 0:
#         Pm10_gs.append(pm10_gs)
#         Time_pm10_gs.append(date_object) 


# Time_o3_gs_KST = []
# for i in range(len(Time_o3_gs)):
#     kst = Time_o3_gs[i] + datetime.timedelta(hours=9)
#     Time_o3_gs_KST.append(kst)
    
    
'''
2)import CMAQ 5.4 data
'''

'''
2-1) import cmaq data
'''
dirw='/Users/beiming_tang/Desktop/Visu_NOAA_CMAQ/CODE/0_surface_map/cmaq5p4_develop/'
pattern = 'Surface_Map_o3.nc'                                                  #change chemical species1
filename = dirw+ pattern
f = Dataset(filename,'r')

lat_wrf  = f.variables['lat'][:]
lon_wrf  = f.variables['lon'][:]
no2_wrf = f.variables['o3'][:]                                                 #change chemical species2

'''
2-2)interpolation at given ground station location
'''
lat_Olympic_Park = 38.89511                                                    #DC
lon_Olympic_Park = -77.03637                                                   #DC

# lat_Olympic_Park = 42.361145                                                   #Boston
# lon_Olympic_Park = -71.057083                                                  #Boston


no2_compare = []
for i in range(1, 225):
    for j in range(1, 393):
        if (lon_wrf[i-1][j-1]-lon_Olympic_Park)*(lon_wrf[i-1][j]-lon_Olympic_Park) < 0 and (lat_wrf[i-1][j]-lat_Olympic_Park)*(lat_wrf[i][j]-lat_Olympic_Park) < 0:          
            x1 = np.abs((lon_wrf[i-1][j-1]-lon_Olympic_Park)/(lon_wrf[i-1][j-1]-lon_wrf[i-1][j]))
            x2 = np.abs((lon_wrf[i-1][j]-lon_Olympic_Park)/(lon_wrf[i-1][j-1]-lon_wrf[i-1][j]))
            
            y1 = np.abs((lat_wrf[i-1][j]-lat_Olympic_Park)/(lat_wrf[i-1][j]-lat_wrf[i][j]))
            y2 = np.abs((lat_wrf[i][j]-lat_Olympic_Park)/(lat_wrf[i-1][j]-lat_wrf[i][j]))
  
            for k in range(len(no2_wrf)):
                a = x2 * no2_wrf[k][i-1][j-1] + x1 * no2_wrf[k][i-1][j]
                b = x2 * no2_wrf[k][i][j-1] + x1 * no2_wrf[k][i][j]
                c = y1 * b + y2 * a
                if c >= 0:
                    no2_compare.append(c)
                else:
                    no2_compare.append(0)                                      #change missing hrs values here3
        

O3_CMAQ54 = no2_compare   #change chemical species4


'''
3)import CMAQ 5.2 data
'''

'''
3-1) import cmaq data
'''
dirw='/Users/beiming_tang/Desktop/Visu_NOAA_CMAQ/CODE/0_surface_map/cmaq5p2_develop/'
pattern = 'Surface_Map_o3.nc'                                                  #change chemical species1
filename = dirw+ pattern
f = Dataset(filename,'r')

lat_wrf  = f.variables['lat'][:]
lon_wrf  = f.variables['lon'][:]
no2_wrf = f.variables['o3'][:]                                                 #change chemical species2

'''
3-2)interpolation at given ground station location
'''
lat_Olympic_Park = 38.89511                                                    #DC
lon_Olympic_Park = -77.03637                                                   #DC

# lat_Olympic_Park = 42.361145                                                   #Boston
# lon_Olympic_Park = -71.057083                                                  #Boston


no2_compare = []
for i in range(1, 225):
    for j in range(1, 393):
        if (lon_wrf[i-1][j-1]-lon_Olympic_Park)*(lon_wrf[i-1][j]-lon_Olympic_Park) < 0 and (lat_wrf[i-1][j]-lat_Olympic_Park)*(lat_wrf[i][j]-lat_Olympic_Park) < 0:          
            x1 = np.abs((lon_wrf[i-1][j-1]-lon_Olympic_Park)/(lon_wrf[i-1][j-1]-lon_wrf[i-1][j]))
            x2 = np.abs((lon_wrf[i-1][j]-lon_Olympic_Park)/(lon_wrf[i-1][j-1]-lon_wrf[i-1][j]))
            
            y1 = np.abs((lat_wrf[i-1][j]-lat_Olympic_Park)/(lat_wrf[i-1][j]-lat_wrf[i][j]))
            y2 = np.abs((lat_wrf[i][j]-lat_Olympic_Park)/(lat_wrf[i-1][j]-lat_wrf[i][j]))
  
            for k in range(len(no2_wrf)):
                a = x2 * no2_wrf[k][i-1][j-1] + x1 * no2_wrf[k][i-1][j]
                b = x2 * no2_wrf[k][i][j-1] + x1 * no2_wrf[k][i][j]
                c = y1 * b + y2 * a
                if c >= 0:
                    no2_compare.append(c)
                else:
                    no2_compare.append(0)                                      #change missing hrs values here3
        

O3_CMAQ52 = no2_compare   #change chemical species4


























        

       
        