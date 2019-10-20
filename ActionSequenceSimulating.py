import chess
import chess.pgn
import helper
import random

class engine:
    def __init__(self):
        self.turn = 0
        self.help = helper.meth()
    
    def play(self, board, tlim):
        if board.turn == chess.WHITE:
            player_col = 1 #this no worky work
        else:
            pcoplayer_col = -1


            # for cur in root,variations:

        best_move = random.choice(movespace)
        self.turn += 1
        # print(type(best_node.move))
        if self.turn > 75:
            return chess.Move.null()
        return best_move

    class branchy:
        def __init__():
            self.node
            self.depth