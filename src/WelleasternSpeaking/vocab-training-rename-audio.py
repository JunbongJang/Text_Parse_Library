# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 19:37:56 2018

@author: JunbongJang
"""

#!/usr/bin/python

import os, sys
# Open a file
path = '/Users/JunbongJang/Desktop/suneung2014/'
for i in range(24,51):
    print(i)
    path_i = path + str(i) + '회차'
    dirs = os.listdir( path_i )
    
    # This would print all the files and directories
    for filename in dirs:
       print (filename)
       if filename[0:3].isdigit():
           os.rename(os.path.join(path_i, filename), os.path.join(path_i, filename[4:]))