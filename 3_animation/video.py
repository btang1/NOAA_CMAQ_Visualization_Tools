#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 02:01:47 2020

@author: beimingtao
"""

import cv2
import numpy as np
import glob
 
img_array = []
for filename in sorted(glob.glob('/Users/beiming_tang/Desktop/Visu_NOAA_CMAQ/CODE/2_spatial_map_per_time/ps_*.png')):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv2.VideoWriter('ps.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 1, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()




