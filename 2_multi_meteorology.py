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

from Ps import PS_CMAQ54,PS_CMAQ52
from Tmp import TEMP_CMAQ54,TEMP_CMAQ52
from Uwnd import UWND_CMAQ54,UWND_CMAQ52
from Vwnd import VWND_CMAQ54,VWND_CMAQ52

base = dt(2019,7,17,0,0,0)  
Time_WRF = [base + datetime.timedelta(hours=x) for x in range(len(PS_CMAQ54))]    # create time_wrf to compare

import matplotlib.dates as mdates
myFmt = mdates.DateFormatter('%m/%d %H') 

fig = plt.subplots(1,1,figsize = (15,10)) 

ax1 = plt.subplot(4,1,1)
ax1.xaxis.set_major_formatter(myFmt)
plt.plot(Time_WRF,PS_CMAQ54,'r',label = 'CMAQ 5.4 develop' )
plt.plot(Time_WRF,PS_CMAQ52,'k',label = 'CMAQ 5.2 develop' )
plt.tick_params(labelbottom = False, bottom = False)
plt.xlim(datetime.datetime(2019,7,17,0,0,0),datetime.datetime(2019,7,17,6,0,0))
plt.ylabel('Pressure \n (Pa)',fontsize = 20)
plt.title('Time Series at DC, source: dynf000*.nc',fontsize = 30)                            #change here for location information
plt.legend(loc='upper left',fontsize = 15)

ax2 = plt.subplot(4,1,2)
ax2.xaxis.set_major_formatter(myFmt)
plt.plot(Time_WRF,TEMP_CMAQ54,'r',label = 'CMAQ 5.4 develop' )
plt.plot(Time_WRF,TEMP_CMAQ52,'k',label = 'CMAQ 5.2 develop' )
plt.tick_params(labelbottom = False, bottom = False)
plt.xlim(datetime.datetime(2019,7,17,0,0,0),datetime.datetime(2019,7,17,6,0,0))
plt.ylabel('TEMP\n (K)',fontsize = 20)
plt.legend(loc='upper left',fontsize = 15)

ax3 = plt.subplot(4,1,3)
ax3.xaxis.set_major_formatter(myFmt)
plt.plot(Time_WRF,UWND_CMAQ54,'r',label = 'CMAQ 5.4 develop' )
plt.plot(Time_WRF,UWND_CMAQ52,'k',label = 'CMAQ 5.2 develop' )
plt.tick_params(labelbottom = False, bottom = False)
plt.xlim(datetime.datetime(2019,7,17,0,0,0),datetime.datetime(2019,7,17,6,0,0))
plt.ylabel('WIND-U\n (m/s)',fontsize = 20)
plt.legend(loc='upper left',fontsize = 15)

ax4 = plt.subplot(4,1,4)
ax4.xaxis.set_major_formatter(myFmt)
plt.plot(Time_WRF,VWND_CMAQ54,'r',label = 'CMAQ 5.4 develop' )
plt.plot(Time_WRF,VWND_CMAQ52,'k',label = 'CMAQ 5.2 develop' )
plt.xlim(datetime.datetime(2019,7,17,0,0,0),datetime.datetime(2019,7,17,6,0,0))
plt.ylabel('WIND-V\n (m/s)',fontsize = 20)
plt.legend(loc='upper left',fontsize = 15)

plt.xlabel('Time',fontsize = 20)
plt.savefig('Meteorology_MTS_DC.png',dpi = 600)























