#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 03:08:18 2021

@author: beimingtao
"""

import numpy as np
import os
from scipy import spatial
import fnmatch
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.basemap import Basemap
import codecs
import datetime
from datetime import datetime as dt
plt.rc('ytick', labelsize=20)    #change y label fontsize
plt.rc('xtick', labelsize=20)    #change y label fontsize

'''
1) import co data cmaq54
'''
dirw='/Users/beiming_tang/Desktop/Visu_NOAA_CMAQ/CODE/0_surface_map/cmaq5p4_develop/'
pattern = 'Surface_Map_temp.nc'                                         #change chemical species
filename = dirw+ pattern
f = Dataset(filename,'r')

Lat_0  = f.variables['lat'][:]
Lon_0  = f.variables['lon'][:]
data_54 = f.variables['temp'][:]                                         #change chemical species

base = dt(2019,7,17,0,0,0)  
Time_CMAQ = [base + datetime.timedelta(hours=x) for x in range(len(data_54))]    


'''
2) import co data cmaq52
'''
dirw='/Users/beiming_tang/Desktop/Visu_NOAA_CMAQ/CODE/0_surface_map/cmaq5p2_develop/'
pattern = 'Surface_Map_temp.nc'                                         #change chemical species
filename = dirw+ pattern
f = Dataset(filename,'r')

# Lat_0  = f.variables['lat'][:]
# Lon_0  = f.variables['lon'][:]
data_52 = f.variables['temp'][:]                                         #change chemical species


'''
4) plot the map
'''
for i in range(len(data_54)):
    data_1 = data_54[i]-data_52[i]                                              
    
    m = Basemap(rsphere=(6378137.00,6356752.3142),projection='lcc', resolution='l',
                llcrnrlat=21, urcrnrlat = 48,llcrnrlon=-123, urcrnrlon =-62,
                lat_1= 20,lat_2= 60,lat_0=40 ,lon_0= -96)                   #Lambert Projection
    fig = plt.subplots(1,1,figsize = (15,12))     
    m.pcolormesh(Lon_0, Lat_0, data_1,latlon=True,vmin = -5, vmax = 5, cmap = 'bwr') 
    
    cb =plt.colorbar(orientation="horizontal")
    cb.set_label('Temperature (K)',fontsize = 30)                                                            #change units
    cb.ax.tick_params(labelsize=30)
    
    m.drawcoastlines(linewidth=1)
    m.drawcountries()
    m.drawstates()
    plt.title('Differnce Map for Temperature CMAQ5.4_develop vs. CMAQ5.2_develop \n@'+str(Time_CMAQ[i]),fontsize=30)
    plt.savefig('diffmap_temp_'+str(i),dpi = 100)
   
                                              




