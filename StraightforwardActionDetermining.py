import chess
import chess.pgn
import helper

class engine:
    def __init__(self):
        self.turn = 0
        self.help = helper.meth()
    
    def play(self, board, tlim):
        # if board.turn == BLACK:
        #     board.mirror() #this no worky work
        
        move_list = self.help.legal_move_list(board)
        
        root = chess.pgn.Game()
        root.setup(board.fen())

        best_score = [-10000] #set the bar low
        list_analysis = []
        for item in move_list:
            child = chess.pgn.GameNode()
            child.parent = root
            child.move = board.parse_san(item)
            score = self.help.board_value(child.board(),1)
            child.comment = score
            list_analysis.append([child.move, score]) #idk if this is neccessary
            root.variations.append(child)

        if self.turn < 2:
            print(list_analysis)


        for cur in root.variations:
            if cur.comment >= best_score:
                # add to list if > 1 or equal
        
        self.turn += 1
        # print(type(best_node.move))
        return best_move