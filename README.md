# ChessEngine (Easter nights project)

*An attempt to write a chess engine using python with zero knowledge what I do*

let's define a "success" as when this thing beats me (my chess.com rating ~1500) 
 

### Some concepts to learn on the way:

- [Castling](https://en.wikipedia.org/wiki/Castling)
- [en passant](https://en.wikipedia.org/wiki/En_passant)
- [python chess GitHub](https://github.com/niklasf/python-chess)
- [python chess docs](https://python-chess.readthedocs.io/en/latest/)
- [Forsyth–Edwards notation](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation)
- [pgn notation](https://en.wikipedia.org/wiki/Portable_Game_Notation)
- [Board representation (computer chess)](https://en.wikipedia.org/wiki/Board_representation_(computer_chess))
- [curl](https://www.prostdev.com/post/the-power-of-curl)
- [minimax](https://en.wikipedia.org/wiki/Minimax)
- [Bellman equation](https://en.wikipedia.org/wiki/Bellman_equation)

### Chess databases:

- [Caissabase](http://caissabase.co.uk/)
- [KingBase (archive)](https://archive.org/details/KingBase2018)

used data: [KingBase2018-pgn.zip 409.3M](https://archive.org/download/KingBase2018)

### AI representation of chess problem

- [G. Hotz twitchchess](https://gitshub.com/geohot/twitchchess)

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
8x8x4 + 1 = 257 bits (vector of 0 or 1)
