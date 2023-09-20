#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:09:26 2019

@author: tangbeiming
"""

import numpy as np
import os
import sys
from netCDF4 import Dataset
import fnmatch

'''
1)read data from WRF-Chen output
'''
dir_data ='/Users/beiming_tang/Desktop/Visu_NOAA_CMAQ/DATA/CMAQ5p2_develop/'
pattern ='dynf*'

wrf_list_raw = fnmatch.filter(os.listdir(dir_data),pattern)
filelist = np.sort(wrf_list_raw)

for i in range(len(filelist)):
    filename = dir_data+filelist[i]
    f = Dataset(filename,'r')

    lat_w = f.variables['lat'][:]
    lon_w = f.variables['lon'][:]-360
    pressure_w = f.variables['pressfc'][:][0]
    temp_w = f.variables['tmp'][:][0][-1]
    u_w = f.variables['ugrd'][:][0][-1]
    v_w = f.variables['vgrd'][:][0][-1]
    
    vmro3_w = f.variables['o3_ave'][:][0][-1]
    vmrco_w = 10**(3)*f.variables['co'][:][0][-1]
    vmrno_w = f.variables['no_ave'][:][0][-1]
    vmrno2_w= f.variables['no2_ave'][:][0][-1]
    pm25_w = f.variables['pm25_ave'][:][0][-1]

    
    '''
    2)write a new netCDF
    '''
    ft = Dataset('BEV_'+filelist[i],'w',format = 'NETCDF4')
     
    ntime = ft.createDimension('ntime',None)
    nlat = ft.createDimension('nlat',225)
    nlon = ft.createDimension('nlon',393)
    
    lat = ft.createVariable('lat','f4',('nlat','nlon'))
    lat.units =f.variables['lat'].units
    lat.description =f.variables['lat'].long_name
    
    lon = ft.createVariable('lon','f4',('nlat','nlon'))
    lon.units =f.variables['lon'].units
    lon.description =f.variables['lon'].long_name

    pm25 = ft.createVariable('pm25','f4',('ntime','nlat','nlon'))
    pm25.units ='ug m^-3'
    pm25.description ='pm2.5'
    
    ps = ft.createVariable('ps','f4',('ntime','nlat','nlon'))
    ps.units ='Pa'
    ps.description ='pressure'
    
    tmp = ft.createVariable('tmp','f4',('ntime','nlat','nlon'))
    tmp.units = 'K'
    tmp.description = 'Temperature'
    
    uwnd = ft.createVariable('uwnd','f4',('ntime','nlat','nlon'))
    uwnd.units =f.variables['ugrd'].units
    uwnd.description ='wind velocity in u direction'
    
    vwnd = ft.createVariable('vwnd','f4',('ntime','nlat','nlon'))
    vwnd.units =f.variables['vgrd'].units
    vwnd.description = 'wind velocity in v direction'
    
    vmro3 = ft.createVariable('o3','f4',('ntime','nlat','nlon'))
    vmro3.units ='ppbv'
    vmro3.description =f.variables['o3_ave'].long_name
    
    vmrco = ft.createVariable('co','f4',('ntime','nlat','nlon'))
    vmrco.units ='ppbv'
    vmrco.description =f.variables['co'].long_name
    
    vmrno = ft.createVariable('no','f4',('ntime','nlat','nlon'))
    vmrno.units = 'ppbv'
    vmrno.description =f.variables['no_ave'].long_name
    
    vmrno2 = ft.createVariable('no2','f4',('ntime','nlat','nlon'))
    vmrno2.units ='ppbv'
    vmrno2.description =f.variables['no2_ave'].long_name
    
 
    '''
    3)input data
    '''
    lat[:,:]= lat_w
    lon[:,:]= lon_w
    pm25[0,:,:] = pm25_w
    ps[0,:,:] = pressure_w
    tmp[0,:,:] = temp_w
    uwnd[0,:,:] = u_w
    vwnd[0,:,:] = v_w
    vmro3[0,:,:] = vmro3_w
    vmrco[0,:,:] = vmrco_w
    vmrno[0,:,:]= vmrno_w
    vmrno2[0,:,:]= vmrno2_w

       
    ft.close()
    f.close()













