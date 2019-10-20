import chess
import re
import random

board  = chess.Board()
leg_move = board.legal_moves

leg_move_str = str(leg_move)

leg_move_list = re.findall(r"\w{2,4}(?=,|\))",leg_move_str)

rnum = random.randint(0,len(leg_move_list)-1)

print(leg_move_list[rnum])