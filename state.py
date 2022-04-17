#!/usr/bin/env python3

from logging import exception
import os
import chess.pgn

# https://archive.org/download/KingBase2018/KingBase2018-pgn.zip
# pgn files in the data folder

# pgn parsing: https://python-chess.readthedocs.io/en/latest/pgn.html
for fn in os.listdir("data"):
    pgn = open(os.path.join("data", fn))
    while 1:
        try:
            game = chess.pgn.read_game(pgn)
            # print(game)
        except Exception: 
            break
        value = {'1/2-1/2':0, '0-1':-1, '1-0':1}[game.headers['Result']]
        print(value)
        '''
        board = game.board()
        for i, move in enumerate(game.mainline_moves()):
            board.push(move)
            # print(i)
            # print(result)
            # print(board)
        exit(0)
        '''
    break

class State(object): 
    def __init__(self):
        self.board = chess.Board()

    def serialize(self):
        # 257 bits according to readme
        pass

    def edges(self):
        return list(self.board.legal_moves)

    def value(self):
        return 1 # all positions are equal for now

if __name__ == "__main__":
    s = State()
    print(s.edges()) 