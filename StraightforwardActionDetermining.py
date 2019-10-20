import chess
import chess.pgn
import helper

class engine:
    def __init__(self):
        self.turn = 0
        self.help = helper.meth()
    
    def play(self, board, tlim):
        move_list = self.help.legal_move_list(board)
        
        root = chess.pgn.Game()
        root.setup(board.fen())

        best_score = -10
        for item in move_list:
            child = chess.pgn.GameNode()
            child.parent = root
            child.move = board.parse_san(item)
            score = self.help.board_value(child.board(),1)
            child.comment = score
            if score > best_score:
                best_score = score
                best_move = child.move
                print(child.comment)

            # root.variations.append(child)

            # print(child.board)
        
        # best_score = 0
        # score = 0
        # best_node = root
        # for cur in root.variations:
            # print(cur.board())
            # print(self.turn)
            # test = self.help.board_value(cur.board(),1)
            # print(test)
            # score = test
            # score = 1 #self.help.board_value(cur.board(),1)
            # if score > best_score:
            #     best_score = score
            #     best_node = cur
        
        self.turn += 1
        # print(type(best_node.move))
        return best_move