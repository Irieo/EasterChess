import chess
import numpy as np

class State(object): 
    def __init__(self, board=None):
        if board is None:
            self.board = chess.Board()
        else: 
            self.board = board

    def serialize(self):
        bstate = np.zeros((64))

        state = np.zeros((8,8,5))
        # state[self.board.ep_square, :, :, 3] = 1

        # 4th column is who's turn it is
        state[:,:,4] = (self.board.turn*1.0)
        print()

        # 257 bits according to readme
        # pp = self.board.shredder_fen()
        # return pp
        return state

    def edges(self):
        return list(self.board.legal_moves)

    def value(self):
        return 1 # all positions are equal for now

if __name__ == "__main__":
    s = State()
    # print(s.edges())