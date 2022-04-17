# ChessEngine (Easter nights project)

*An attempt to write a chess engine with zero knowledge what I do*

let's define a "success" as when this thing beats me (my chess.com rating ~1500)  

### Some concepts to learn on this way:
- [minimax](https://en.wikipedia.org/wiki/Minimax)
- [Castling](https://en.wikipedia.org/wiki/Castling)
- [en passant](https://en.wikipedia.org/wiki/En_passant)
- [python chess GitHub](https://github.com/niklasf/python-chess)
- [python chess docs](https://python-chess.readthedocs.io/en/latest/)
- [Forsyth–Edwards Notation](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation)
- [Board representation (computer chess)](https://en.wikipedia.org/wiki/Board_representation_(computer_chess))

---
### AI representation 
- [G. Hotz twitchchess](https://github.com/geohot/twitchchess)

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