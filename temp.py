import chess
import re
import random
import helper

# print('\n\n\n\n\n')
# piece_val = { 'P': 100, 'N': 250, 'B': 300, 'R': 500, 'Q': 1000, 'K': 100000, 'p': -100, 'n': -250, 'b': -300, 'r': -500, 'q': -1000, 'k': -100000}
board  = chess.Board()
# board.set_epd("1k1r4/pp1b1R2/3q2pp/4p3/2B5/4Q3/PPP2B2/2K5 b - - bm Qd1+; id \"BK.01\";")
# pmap = board.piece_map()
# value = 0
# col = 1
# for key in pmap:
#     # print(key)
#     value += piece_val[pmap[key].symbol()]*col
#     # print(pmap[key].symbol())
# print(value)
