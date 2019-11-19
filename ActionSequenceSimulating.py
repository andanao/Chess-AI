import chess
import chess.pgn
import helper
import random
from chess_debug import print_to_debug

class engine:
    def __init__(self):
        self.turn = 0
        self.help = helper.meth()
    
    def play(self, board, tlim):
        """ChessEngine """
        if board.turn == chess.WHITE:
            player_col = 1 #this no worky work
        else:
            player_col = -1
        
        # root = self.help.grow_twigs(board,player_col)
        test_space = self.help.tree2(board,player_col)
        # print_to_debug(test_space)
        # for cur in root.variations:
        #     child = self.help.grow_twigs(cur.board(),-player_col)
        #     for item in child.variations:
        #         test_space.append([cur.comment[0], cur.comment[1] - item.comment[1]])
        # print(len(test_space))
        
        best_score = [-10000] #set the bar low
        movespace = [test_space[0][0]]
        for i in range(len(test_space)):
            if test_space[i][1] >= best_score[0]:
                if test_space[i][1] > best_score[0]:
                    best_score.clear()
                    movespace.clear()
                best_score.append(test_space[i][1])
                movespace.append(test_space[i][0])
                

        best_move = random.choice(movespace)
        self.turn += 1
        # print(type(best_node.move))
        if self.turn > 75:
            return chess.Move.null()
        return best_move
