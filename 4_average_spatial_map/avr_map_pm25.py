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
1) import co data original
'''


dirw='/Users/beiming_tang/Desktop/Visu_NOAA_CMAQ/CODE/0_surface_map/cmaq5p4_develop/'
pattern = 'Surface_Map_pm25.nc'                                                  #change chemical species
filename = dirw+ pattern
f = Dataset(filename,'r')

Lat_0  = f.variables['lat'][:]
Lon_0  = f.variables['lon'][:]
data_0 = f.variables['pm25'][:]                                                  #change chemical species

'''
2) calculate average map
'''
data_sum = data_0[0]
for i in range(1,len(data_0 )):
    data_sum += data_0[i]
data_avr = data_sum/len(data_0)

base = dt(2019,7,17,0,0,0)  
Time_CMAQ = [base + datetime.timedelta(hours=x) for x in range(len(data_0))]   
'''
2) plot the map
'''                                            

m = Basemap(rsphere=(6378137.00,6356752.3142),projection='lcc', resolution='l',
            llcrnrlat=21, urcrnrlat = 48,llcrnrlon=-123, urcrnrlon =-62,
            lat_1= 20,lat_2= 60,lat_0=40 ,lon_0= -96)                          #Lambert Projection
fig = plt.subplots(1,1,figsize = (15,12))     
m.pcolormesh(Lon_0, Lat_0, data_avr,latlon=True, vmin=0, vmax=1E-3, cmap = 'jet')  #change chemical species range

cb =plt.colorbar(orientation="horizontal")
cb.set_label('$PM_{2.5}$ (\u03bcg/$m^3$)',fontsize = 30)                                        #change chemical species                                                          #change units
cb.ax.tick_params(labelsize=30)

m.drawcoastlines(linewidth=1)
m.drawcountries()
m.drawstates()
plt.title('Averages for $PM_{2.5}$ from '+ str(Time_CMAQ[0])+'\nto '+ str(Time_CMAQ[-1]),fontsize=30) #change chemical species
plt.savefig('avr_pm25',dpi = 100)                                               #change chemical species
   
                                          




