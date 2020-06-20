import chess
import random
import re
import helper

class engine:
    """
    Chess engine that makes a random move
    """
    # needs initializer
    def __init__(self,tlim):
        self.turn = 0
        self.tlim = tlim
    
    def play(self, board, tlim):
        help = helper.meth()
        if self.turn < 50:
            leg_move_list = help.legal_move_list(board)
            random_num = random.randint(0,len(leg_move_list)-1)
            try:
                optimal_play = board.parse_san(leg_move_list[random_num])
                # break
            except:
                print('Broken at')
                print(board.legal_moves)
                # print(leg_move_list)
                print(leg_move_list[random_num])
        else:
            optimal_play = chess.Move.null()

        self.turn += 1
        return optimal_play
