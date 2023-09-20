#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 02:53:00 2020

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
plt.rc('ytick', labelsize=20)    #change y label fontsize
plt.rc('xtick', labelsize=20)    #change y label fontsize

from PM25 import PM25_CMAQ54,PM25_CMAQ52
from O3 import O3_CMAQ54,O3_CMAQ52
from NO import NO_CMAQ54,NO_CMAQ52
from NO2 import NO2_CMAQ54,NO2_CMAQ52
from CO import CO_CMAQ54,CO_CMAQ52

base = dt(2019,7,17,0,0,0)  
Time_WRF = [base + datetime.timedelta(hours=x) for x in range(len(O3_CMAQ54))]    # create time_wrf to compare

import matplotlib.dates as mdates
myFmt = mdates.DateFormatter('%m/%d %H') 

fig = plt.subplots(1,1,figsize = (15,10)) 

ax1 = plt.subplot(5,1,1)
ax1.xaxis.set_major_formatter(myFmt)
plt.plot(Time_WRF,O3_CMAQ54,'r',label = 'CMAQ 5.4 develop' )
plt.plot(Time_WRF,O3_CMAQ52,'k',label = 'CMAQ 5.2 develop' )
plt.tick_params(labelbottom = False, bottom = False)
plt.xlim(datetime.datetime(2019,7,17,0,0,0),datetime.datetime(2019,7,17,6,0,0))
plt.ylabel('O$_3$ \n (ppbv)',fontsize = 20)
plt.title('Time Series at DC, source: dynf000*.nc',fontsize = 30)                            #change here for location information
plt.legend(loc='upper left',fontsize = 15)

ax2 = plt.subplot(5,1,2)
ax2.xaxis.set_major_formatter(myFmt)
plt.plot(Time_WRF,NO_CMAQ54,'r',label = 'CMAQ 5.4 develop' )
plt.plot(Time_WRF,NO_CMAQ52,'k',label = 'CMAQ 5.2 develop' )
plt.tick_params(labelbottom = False, bottom = False)
plt.xlim(datetime.datetime(2019,7,17,0,0,0),datetime.datetime(2019,7,17,6,0,0))
plt.ylabel('NO \n (ppbv)',fontsize = 20)
plt.legend(loc='upper left',fontsize = 15)

ax3 = plt.subplot(5,1,3)
ax3.xaxis.set_major_formatter(myFmt)
plt.plot(Time_WRF,NO2_CMAQ54,'r',label = 'CMAQ 5.4 develop' )
plt.plot(Time_WRF,NO2_CMAQ52,'k',label = 'CMAQ 5.2 develop' )
plt.tick_params(labelbottom = False, bottom = False)
plt.xlim(datetime.datetime(2019,7,17,0,0,0),datetime.datetime(2019,7,17,6,0,0))
plt.ylabel('$NO_2$\n (ppbv)',fontsize = 20)
plt.legend(loc='upper left',fontsize = 15)

ax4 = plt.subplot(5,1,4)
ax4.xaxis.set_major_formatter(myFmt)
plt.plot(Time_WRF,CO_CMAQ54,'r',label = 'CMAQ 5.4 develop' )
plt.plot(Time_WRF,CO_CMAQ52,'k',label = 'CMAQ 5.2 develop' )
plt.tick_params(labelbottom = False, bottom = False)
plt.xlim(datetime.datetime(2019,7,17,0,0,0),datetime.datetime(2019,7,17,6,0,0))
plt.ylabel('CO\n (ppbv)',fontsize = 20)
plt.legend(loc='upper left',fontsize = 15)

ax5 = plt.subplot(5,1,5)
ax5.xaxis.set_major_formatter(myFmt)
plt.plot(Time_WRF,PM25_CMAQ54,'r',label = 'CMAQ 5.4 develop' )
plt.plot(Time_WRF,PM25_CMAQ52,'k',label = 'CMAQ 5.2 develop' )
plt.xlim(datetime.datetime(2019,7,17,0,0,0),datetime.datetime(2019,7,17,6,0,0))
plt.ylabel('$PM_{2.5}$\n (\u03bcg/$m^3$)',fontsize = 20)
plt.xlabel('Time',fontsize = 20)
plt.legend(loc='upper left',fontsize = 15)

plt.savefig('Air_Pollutants_MTS_DC.png',dpi = 600)























