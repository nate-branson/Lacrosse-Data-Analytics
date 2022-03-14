### main.py
'''
author:             Nathan Branson
description:        main function for utilizing library
'''

from read_files import *
from analysis import *

def main():
    game        = "Example"
    date        = "Jan1"
    data, _     = read_file('data/' + game + '/' + game + '.csv')
    shooters    = data['shooter']
    players = []
    for i in shooters:
        if not i in players:
            players.append(i)

    # individual players
    for i in players:
        plot_shot_locs(data, player = i, game = game, date = date, extra = True, pic_dir='data')
    # full team
    plot_shot_locs(data, player = -1, game = game, date = date, pic_dir='data')


if __name__ == '__main__':
    main()
