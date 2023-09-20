#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 23:02:12 2020

@author: beimingtao
"""

import os

pattern_list = []
for i in range(0,10):   #change here
    pattern_list.append(str(i))
    
#pattern = '11'

for pattern in pattern_list:
    os.rename(r'./co_'+pattern+'.png',r'./co_0'+pattern+'.png')   #change here