
#Visualization.py
'''
author:             Nathan Branson
description:        contains functions for field and goal visualizations 
'''

import matplotlib.pyplot as plt
import matplotlib as mpl


######## Make field #######
# description:  visualization of field for plotting points
# 
# arguments:    size = "half" (string)("half", "full") : shows either half or full field 
#               extra = False (bool) : plots dotted lines at 5, 10, and 15 yds.
#       
# returns:      fig
#               ax of the field
#
# TODO:         

def make_field(size="half", extra = False):

    if   size == "half":
        fig, ax = plt.subplots(figsize=(20,15))
        plt.xlim([-32,32])
        plt.ylim([-18,42])
    elif size == "full":
        fig, ax = plt.subplots(figsize=(7,15))

        plt.xlim([-32,32])
        plt.ylim([-18,97])

    crease1 = plt.Circle((0,0),3,color='black', fill=False)
    crease2 = plt.Circle((0,80),3,color='black', fill=False)
    ax.add_patch(crease1)
    ax.add_patch(crease2)


    # box lines
    x, y = [-30, 30], [20,20]
    plt.plot(x, y, color = 'black')
    x, y = [-20,-20], [-15,20]
    plt.plot(x, y, color = 'black')
    x, y = [20, 20], [-15,20]
    plt.plot(x, y, color = 'black')
    x, y = [-30, 30], [60,60]
    plt.plot(x, y, color = 'black')
    x, y = [-20,-20], [60,95]
    plt.plot(x, y, color = 'black')
    x, y = [20, 20], [60,95]
    plt.plot(x, y, color = 'black')
    if extra:
        x, y = [-20, 20], [15,15]
        plt.plot(x, y, 'k:')
        x, y = [-20, 20], [10,10]
        plt.plot(x, y, 'k:')
        x, y = [-20, 20], [5,5]
        plt.plot(x, y, 'k:')

    # midline
    x, y = [-30, 30], [40,40]
    plt.plot(x, y, color = 'black')

    #endline
    x, y = [-30, 30], [-15,-15]
    plt.plot(x, y, color = 'black')
    x, y = [-30, 30], [95,95]
    plt.plot(x, y, color = 'black')

    #sidelines
    x, y = [-30, -30], [-15,95]
    plt.plot(x, y, color = 'black')
    x, y = [ 30,  30], [-15,95]
    plt.plot(x, y, color = 'black')

    return fig, ax


######## make_goal #######
# description:  visualization of 6x6 lacrosse goal
# 
# arguments:          
# 
# returns:      fig of field
#               ax of field
#
# TODO:         

def make_goal():
    fig, ax = plt.subplots(figsize=(7,7))

    plt.xlim([-1,7])
    plt.ylim([-1,7])
    x, y = [0, 6], [0,0]
    plt.plot(x, y, color = 'orange')
    x, y = [0,6], [6,6]
    plt.plot(x, y, color = 'orange')
    x, y = [6, 6], [0,6]
    plt.plot(x, y, color = 'orange')
    x, y = [0, 0], [0,6]
    plt.plot(x, y, color = 'orange')

    return fig, ax