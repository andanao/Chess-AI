import chess
import re
import random
import helper

# print('\n\n\n\n\n')
board  = chess.Board()
player_col = 1
board.push_san("e4")
piece_val = { 'P': 100, 'N': 250, 'B': 300, 'R': 500, 'Q': 1000, 'K': 100000, 'p': -100, 'n': -250, 'b': -300, 'r': -500, 'q': -1000, 'k': -100000}
# board.set_epd("1k1r4/pp1b1R2/3q2pp/4p3/2B5/4Q3/PPP2B2/2K5 b - - bm Qd1+; id \"BK.01\";")

loc_val = {
    'P' : (
        0,0,0,0,0,0,0,0,
        1,1,1,1,1,1,1,1,
        2,2,2,2,2,2,2,2,
        3,3,3,3,3,3,3,3,
        4,4,4,4,4,4,4,4,
        5,5,5,5,5,5,5,5,
        6,6,6,6,6,6,6,6,
        7,7,7,7,7,7,7,7,
        9,9,9,9,9,9,9,9,
    )
}
value = 0
pmap = board.piece_map()
for key in pmap:
    peice = pmap[key]
    value += piece_val[peice.symbol()]*player_col
    if peice.color:
        

print(value)
print(board)