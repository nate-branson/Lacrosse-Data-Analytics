### analysis.py
'''
author:             Nathan Branson
description:        contains functions for plotting shooting locations and 
                    shooting percentages.

DATA: (see Documentation.pdf for full descriptions)
    shot_num:       int
    shooter:        int
    goalie_hand:    R=0;L=1
    Hand:           R=0;L=1
    type_shot_0:    OH=0;SA=1;UH=2;BH=3;BTB=4;twister=5
    type_shot_1:    Stationary=0;OtR=1;QS=2
    loc_x:          [-20,20]
    loc_y:          [0,20]
    dist:           float
    loc_goal:       [0,29] (subject to change)
    result:         goal=0;save=1;miss=2;pipe=3;blocked=4
    screened:       Y=0;N=1;N/A=2
    HUDL Timestamp: float
    Notes:          string
'''

from cmath import sqrt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import pathlib
from visualization import *


def shot_percentage(data, show=True, hand="both"):

    #shot_data = data['result']
    goals = 0
    shots = 0
    sog = 0
    shot_per = 0
    for i in data:
        if i == 0:
            goals += 1
        if i == 0 or i == 1:
            sog += 1
        shots += 1

    shot_per = (goals/shots) * 100
    sog_per = (sog/shots) * 100

    if show:
        print("goal per: ", goals, "/", shots)
        print(round(shot_per, 2), "%")
        print()
        print("shots on goal per: ", sog, "/", shots)
        print(round(sog_per, 2), "%")
    
    return goals, shot_per, sog, sog_per, shots

def plot_shot_locs(data, shot_hand='B', max_dist=100, min_dist=-20, player = -1, game = "", extra = False, date = ""):
    # hand: Both-B ; Right-R ; Left-L

    field = make_field(size = "half", extra = True)
    fig = field[0]
    ax = field[1]

    data_loc_x  =   data['loc_x']
    data_loc_y  =   data['loc_y']
    shooters    =   data['shooter']
    data_dist   =   data['dist']
    hand_arr    =   data['shot_hand']
    result      =   data['result']#.tolist()
    loc_goal    =   data['loc_goal']
    hand        =   data['shot_hand']
    type_shot_0 =   data['type_shot_0']
    type_shot_1 =   data['type_shot_1']

    # colors for goal, save, miss, block, pipe
    make    = 'green'
    miss    = 'purple'
    save    = 'red'
    block   = 'blue'
    pipe    = 'orange'
    
    loc_xs, loc_ys, new_result, new_loc_goal, new_hand = [], [], [], [], []
    new_type_shot_0, new_type_shot_1 = [], []

    if player < 0:
        loc_xs          = data_loc_x
        loc_ys          = data_loc_y
        new_result      = result
        new_loc_goal    = loc_goal
        new_hand        = hand

    else: 
        for i in range(len(shooters)):
            if shooters[i] == player:
                loc_xs.append(data_loc_x[i])
                loc_ys.append(data_loc_y[i])
                new_result.append(result[i])
                new_hand.append(hand[i])
                if loc_goal[i]>-1:
                    new_loc_goal.append(int(loc_goal[i]))
                else:
                    new_loc_goal.append('N')
                if(type_shot_0[i]>-1):
                    new_type_shot_0.append(int(type_shot_0[i]))
                    new_type_shot_1.append(int(type_shot_1[i]))
                else:
                    new_type_shot_0.append('N')
                    new_type_shot_1.append('N')

    goals, shot_per, sog, sog_per, shots = shot_percentage(new_result, show = False)
        
    loc_x, loc_y, new_new_result, new_new_hand = [], [], [], []

    for i in new_hand:
        if i == 0:
            new_new_hand.append('R')
        elif i == 1:
            new_new_hand.append('L')
        else:
            new_new_hand.append('N')

    if shot_hand == 'R':
        for i in range(len(data_loc_x)):
            if hand_arr[i,1] == 0:
                loc_x.append(loc_xs[i])
                loc_y.append(loc_ys[i])
                new_new_result.append(new_result[i])
    elif shot_hand == 'L':
        for i in range(len(data_loc_x)):
            if hand_arr[i] == 1:
                loc_x.append(loc_xs[i])
                loc_y.append(loc_ys[i])
                new_new_result.append(new_result[i])
    else:
        loc_x = loc_xs
        loc_y = loc_ys
        new_new_result = new_result
    
    loc_x_ma, loc_y_ma = [], [] # make
    loc_x_mi, loc_y_mi = [], [] # miss
    loc_x_sa, loc_y_sa = [], [] # save
    loc_x_pi, loc_y_pi = [], [] # pipe
    loc_x_bl, loc_y_bl = [], [] # block

    for i in range(len(new_new_result)):
        if new_new_result[i]==0:
            loc_x_ma.append(loc_x[i])
            loc_y_ma.append(loc_y[i])
        elif new_new_result[i] == 1:
            loc_x_sa.append(loc_x[i])
            loc_y_sa.append(loc_y[i])
        elif new_new_result[i] == 2:
            loc_x_mi.append(loc_x[i])
            loc_y_mi.append(loc_y[i])
        elif new_new_result[i] == 3:
            loc_x_pi.append(loc_x[i])
            loc_y_pi.append(loc_y[i])
        else:
            loc_x_bl.append(loc_x[i])
            loc_y_bl.append(loc_y[i])

    dist_arr = []

    j = 0
    for i in range(len(loc_x)):
        dist = sqrt((loc_x[i]**2)+(loc_y[i])**2).real
        dist_arr.append(round(dist, 2))
        '''if dist >= min_dist and dist <= max_dist:
            loc_x[j] = loc_x[i]
            loc_y[j] = loc_y[i]
            j += 1'''
    avg_dist = round(sum(dist_arr)/len(dist_arr),2)

    ax.scatter(loc_x_ma, loc_y_ma, color=make,  alpha=.5, edgecolors="black", s=60, label='goal' )
    ax.scatter(loc_x_sa, loc_y_sa, color=save,  alpha=.5, edgecolors="black", s=60, label='save' )
    ax.scatter(loc_x_mi, loc_y_mi, color=miss,  alpha=.5, edgecolors="black", s=60, label='miss' )
    ax.scatter(loc_x_bl, loc_y_bl, color=block, alpha=.5, edgecolors="black", s=60, label='block')
    ax.scatter(loc_x_pi, loc_y_pi, color=pipe,  alpha=.5, edgecolors="black", s=60, label='pipe' )


    # text box showing shooting percentages and average distance
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    textstr = '\n'.join((r'goals: $\frac{%d}{%d}=%.2f$' % (goals,shots,round(shot_per, 2), ), r'shots on goal: $\frac{%d}{%d}=%.2f$' % (sog,shots,round(sog_per, 2), )
    , r'avg distance shot: $%.2f$' % (round(avg_dist, 2), )))
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)
    ax.legend(loc = [0.88, 0.8155])

    # title of chart
    if game == "":
        if player>-1:
            plt.title(r'Shot Chart for #%d' % player)
            text = (r'../Messiah_Shot/Shot_%d.png' % player)
            plt.savefig(text)
        else:
            plt.title("Shot Chart Team")
            plt.savefig('../Messiah_Shot/Shot_team.png')
    else:
        if player>-1:
            text = '\n'.join([r'Shot Chart for #%d' % player, game])
            plt.title(text)
            text = r'../Messiah_Shot/' + game + '/' + date + r'_Shot_' + game + r'_%d.png' % player
            
        else:
            text = '\n'.join([r'Shot Chart for Team', game])
            plt.title(text)
            text = '../Messiah_Shot/' + game + '/' + date + '_Shot_'+game+'_team.png'
            print(text)
            plt.savefig(text)


    if extra:
        for i, txt in enumerate(new_loc_goal):
            ax.annotate(txt, (loc_x[i]+.1, loc_y[i]+.1))
        for i, txt in enumerate(new_new_hand):
            ax.annotate(txt, (loc_x[i]+.85, loc_y[i]+.1))
        for i, txt in enumerate(new_type_shot_0):
            ax.annotate(txt, (loc_x[i]+1.35, loc_y[i]+.1))
        for i, txt in enumerate(new_type_shot_1):
            ax.annotate(txt, (loc_x[i]+1.85, loc_y[i]+.1))
        for i, txt in enumerate(dist_arr):
            ax.annotate(txt, (loc_x[i]+2.3, loc_y[i]+.1))
        im = plt.imread('images/goal.png') # insert local path of the image.
        newax = fig.add_axes([0.8,0.8,0.2,0.2], anchor='NE', zorder=1)
        newax.imshow(im)
        newax.axis('off')        

    print(text)
    plt.savefig(text)


def plot_goal_locs(data):#, fig):
    goal = make_goal()
    #ax = fig[1]
    # x, y

    spots = []
    xv, yv = 0, 1.5
    for i in range(4):
        xh,yh = 0, 1.5
        for j in range(4):
            spots.append([[xv,yv],[xh,yh]]) 
            xh = xh  +1.5
            yh = yh + 1.5
        xv = xv  +1.5
        yv = yv + 1.5

    for i in range(len(spots)):
        rect = mpl.patches.Rectangle((spots[i][0][0],
                spots[i][1][0]),1.5,1.5,edgecolor = 'black', color = None,
                linewidth = 2, facecolor = 'red')
        plt.gca().add_patch(rect)


    plt.show()
