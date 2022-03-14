### read_files.py
'''
author:             Nathan Branson
description:        contains functions for converting csv files to pandas lists.
'''

import pandas as pd
import pathlib

######## read_file #######
# description:  reads a single file
# 
# arguments:    file (string) : file name
#               show = False (bool) : prints data
#       
# returns:      data from file read
#               shape of data 
#
# TODO:  

def read_file(file, show = False):
    data = pd.read_csv(file)
    shape = data.shape

    if show:
        print(data)

    return data, shape


######## read_file #######
# description:  reads multiple files in a dir
# 
# arguments:    dir(string) : dir with files to reade
#               show = False (bool) : prints data
#       
# returns:      data combined from files read
#               shape of data 
#
# TODO:  
def read_multi_files(dir, show = False):
    data = []
    for path in pathlib.Path(dir).iterdir():
        if path.is_file():
            current_file = open(path, "r")
            data_file, _ = read_file(current_file)
            data.append(data_file)
    data = pd.concat(data,ignore_index=True)
    shape = data.shape

    if show:
        print(data)
    return data, shape