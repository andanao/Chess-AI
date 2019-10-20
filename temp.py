import chess
import re
import random
import helper

# print('\n\n\n\n\n')
board  = chess.Board()
pmap = board.piece_map()
for key in pmap:
    print(key)
# print(board.piece_map())
# print(board)
# print(pmap['0'])
# board.pieces('p',chess.BLACK)
# print(board.pieces('P','WHITE'))