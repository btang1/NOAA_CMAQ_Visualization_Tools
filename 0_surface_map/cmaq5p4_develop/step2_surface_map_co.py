#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 13:28:17 2019

@author: tangbeiming
"""

import numpy as np
import os
import sys
from netCDF4 import Dataset
import fnmatch
import datetime
from datetime import datetime

'''
1)read data from WRF-Chen output, BEV_
'''
dir_data ='./'
pattern ='BEV_dynf*'

wrf_list_raw = fnmatch.filter(os.listdir(dir_data),pattern)
filelist = np.sort(wrf_list_raw)


ft = Dataset(('Surface_Map_'+"co.nc"),'w',format = 'NETCDF4')                # change chemicals name here
ntime = ft.createDimension('ntime',len(filelist))
nlat = ft.createDimension('nlat',225)
nlon = ft.createDimension('nlon',393)

time_new = ft.createVariable('time','S1',('ntime',))
time_new.units =''
time_new.description =''

lat = ft.createVariable('lat','f4',('nlat','nlon'))
lat.units =''
lat.description =''

lon = ft.createVariable('lon','f4',('nlat','nlon'))
lon.units =''
lon.description =''

vmrno2 = ft.createVariable('co','f4',('ntime','nlat','nlon'))                # change chemicals name here
vmrno2.units ='ppbv'                                                         # change unit here
vmrno2.description =''
    
for i in range(len(filelist)):

    filename = dir_data+filelist[i]
    f = Dataset(filename,'r')
    
    time_w = filelist[i].replace('BEV_dynf','')
    lat_w = f.variables['lat'][:]
    lon_w = f.variables['lon'][:]
    vmrno2_w= f.variables['co'][0,:]                                       #change chemical variables here
    
    time_new[:] = time_w
    lat[:,:]= lat_w
    lon[:,:]= lon_w
    vmrno2[i,:,:] = vmrno2_w
    

        
    f.close()  
ft.close()
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
