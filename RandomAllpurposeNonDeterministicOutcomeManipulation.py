import chess
import random
import re
import helper

class engine:
    """
    Chess engine that makes a random move
    """
    # needs initializer
    def __init__(self):
        pass
    
    def play(self, board, tlim):
        help = helper.meth()
        leg_move_list = help.legal_move_list(board)
        random_num = random.randint(0,len(leg_move_list)-1)
        optimal_play = board.parse_san(leg_move_list[random_num])
        return optimal_play
