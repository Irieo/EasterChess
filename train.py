#!/usr/bin/env python3

# https://archive.org/download/KingBase2018/KingBase2018-pgn.zip
# pgn files in the data folder

import os
import chess.pgn
from state import State
# def shredder_fen_to_vec(x): 

# pgn parsing: https://python-chess.readthedocs.io/en/latest/pgn.html
for fn in os.listdir("data"):
    pgn = open(os.path.join("data", fn))
    while 1:
        try:
            game = chess.pgn.read_game(pgn)
            # print(game)
        except Exception: 
            break

        # define Values
        value = {'1/2-1/2':0, '0-1':-1, '1-0':1}[game.headers['Result']]
        print(value)

        # Iterate through all moves and play them on a board
        board = game.board()
        for i, move in enumerate(game.mainline_moves()):
            board.push(move)

        # extract positions
        print(value, State(board).serialize())

    break