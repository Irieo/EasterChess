#!/usr/bin/env python3

from turtle import shape
import numpy as np
from torch.utils.data import Dataset

'''
from https://pytorch.org/tutorials/beginner/basics/data_tutorial.html
custom Dataset class must implement three functions: 
__init__ 
__len__
__getitem__
'''

class ChessValueDataset(Dataset):

    def __init__(self):
        data = np.load("processed/dataset_1k.npz")
        self.X = data["arr_0"]
        self.Y = data["arr_1"]
        
        # print(self.X.shape) -> (1134, 8, 8)
        # print(self.Y.shape) -> (1134,)

    def __len__(self):
        return self.X.shape[0]

    def __getitem__(self, idx):
        return {"X": self.X[idx], "Y": self.Y[idx]}

chess_dataset = ChessValueDataset()