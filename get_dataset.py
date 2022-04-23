#!/usr/bin/env python3

import os
import chess.pgn
import h5py 
import numpy as np
from state import State
# from webbrowser import get

# def shredder_fen_to_vec(x): 

def get_dataset(num_samples=None):

    X,Y = [], []
    gn = 0

    # pgn parsing: https://python-chess.readthedocs.io/en/latest/pgn.html
    # https://archive.org/download/KingBase2018/KingBase2018-pgn.zip
    # pgn files in the data folder
    for fn in os.listdir("data"):
        pgn = open(os.path.join("data", fn))
        while 1:
            try:
                game = chess.pgn.read_game(pgn)
            except Exception: 
                break

            # define Value
            value = {'1/2-1/2':0, '0-1':-1, '1-0':1, '*':0}[game.headers['Result']]
            # print(value)
            
            # Iterate through all moves and play them on a board
            board = game.board()
            for i, move in enumerate(game.mainline_moves()):
                board.push(move)
                # extract positions
                ser = State(board).serialize()[:,:,0]
                X.append(ser)
                Y.append(value)
            print ("parsing game %d, got %d examples" % (gn, len(X)))
            # num_samples=1000 -> parsing game 12, got 1134 examples

            if num_samples is not None and len(X) > num_samples:
                return X, Y 
            gn += 1
        X = np.array(X)
        Y = np.array(Y)
        return X, Y

if __name__ == "__main__":
    # X, Y = get_dataset(1e3)
    # np.savez("processed/dataset_1k.npz", X, Y)
    
    X, Y = get_dataset()
    np.savez("processed/dataset_full.npz", X, Y)