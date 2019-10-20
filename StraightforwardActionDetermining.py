import chess
import helper

class engine:
    def __init__(self):
        self.turn = 0
        self.help = helper.meth()
    
    def play(self, board, tlim):

