import chess
import random
import re
import helper

class engine:
    # needs initializer
    def __init__(self):
        pass
    
    def play(self, board, tlim):
        leg_move_list = helper.meth.legal_move_list(board)
        random_num = random.randint(0,len(leg_move_list)-1)
        optimal_play = board.parse_san(leg_move_list[random_num])
        return optimal_play
