import chess
import re
import random
import helper

print('\n\n\n\n\n')
board  = chess.Board()
board.set_epd("1k1r4/pp1b1R2/3q2pp/4p3/2B5/4Q3/PPP2B2/2K5 b - - bm Qd1+; id \"BK.01\";")
chelp = helper.meth()
bval = chelp.board_value(board,1)
print(bval)
