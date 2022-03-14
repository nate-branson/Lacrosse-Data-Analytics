### main.py
'''
author:             Nathan Branson
description:        main function for utilizing library
'''

from read_files import *
from analysis import *

def main():
    game        = "Kings"
    date        = "Mar2"
    data, _     = read_file('../Messiah_Shot/' + game + '/' + date + '_Shot_' + game + '.csv')
    shooters    = data['shooter']
    players = []
    for i in shooters:
        if not i in players:
            players.append(i)
    #players.append(-1)
    
    #data = read_multi_files('../Messiah_Shot/Shot_Charts')
    #print(data)
    for i in players:
        plot_shot_locs(data, player = i, game = game, date = date, extra = True)
    plot_shot_locs(data, player = -1, game = game, date = date)
    

    #plot_goal_locs(data)


if __name__ == '__main__':
    main()
