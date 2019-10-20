import chess
import re
import random
import helper

# print('\n\n\n\n\n')
piece_val = { 'P': 100, 'N': 250, 'B': 300, 'R': 500, 'Q': 1000, 'K': 100000, 'p': -100, 'n': -250, 'b': -300, 'r': -500, 'q': -1000, 'k': -100000}
board  = chess.Board()
pmap = board.piece_map()
value = 0
for key in pmap:
    # print(key)
    value += piece_val[pmap[key].symbol()]
    # print(pmap[key].symbol())
print(value)
# print(board.piece_map())
# print(board)
# print(pmap['0'])
# board.pieces('p',chess.BLACK)
# print(board.pieces('P','WHITE'))