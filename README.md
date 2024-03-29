# ChessEngine (Easter nights project)

*An attempt to write a chess engine using python with zero knowledge what I do*

let's define a "success" as when this thing beats me (chess.com rating is at 1500) 
 
On a background: it is a fun way to refresh knowledge of python, especially data manipulations, which I need for my research. 

### credits
this project is eventually based on [G. Hotz twitchchess](https://gitshub.com/geohot/twitchchess) GitHub repo and my reverse engineering attempt to grasp how things work.

### Some concepts to learn on the way:

- [Castling](https://en.wikipedia.org/wiki/Castling)
- [en passant](https://en.wikipedia.org/wiki/En_passant)
- [python chess GitHub](https://github.com/niklasf/python-chess)
- [python chess docs](https://python-chess.readthedocs.io/en/latest/)
- [Forsyth–Edwards notation](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation)
- [pgn notation](https://en.wikipedia.org/wiki/Portable_Game_Notation)
- [Board representation (computer chess)](https://en.wikipedia.org/wiki/Board_representation_(computer_chess))
- [curl](https://www.prostdev.com/post/the-power-of-curl)
- [python data types](https://jakevdp.github.io/PythonDataScienceHandbook/02.01-understanding-data-types.html)
- [visual for numpy 3D arrays](https://jalammar.github.io/visual-numpy/)
- [minimax](https://en.wikipedia.org/wiki/Minimax)
- [Bellman equation](https://en.wikipedia.org/wiki/Bellman_equation)
- [h5py](https://docs.h5py.org/en/stable/index.html)

### Chess databases:

- [Caissabase](http://caissabase.co.uk/)
- [KingBase (archive)](https://archive.org/details/KingBase2018)

used data: [KingBase2018-pgn.zip 409.3M](https://archive.org/download/KingBase2018)

### interesting but eventually not useful:

- [CUDA](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)

### AI framework
- [pytorch](https://pytorch.org/)
- [pytorch docs Dataset](https://pytorch.org/tutorials/beginner/basics/data_tutorial.html)

### notes 

Objective Value: V = f(state) 

let's assume:
- V = -1 black wins board state
- V = 0 draw board state
- V = 1 white wins board state 

State(Board):

Pieces (2 + 7*2 = 16):
- Universal
    - Blank
    - Blank (en passant - target square = 64bits)
- Pieces 
    - Pawn
    - Bishop
    - Knight
    - Rook (can castle)
    - Queen
    - King

Extra state:
- To move

Neurons:
- 8x8x4 + 1 = 257 bits (vector of 0 or 1)
- 8x8x5 
