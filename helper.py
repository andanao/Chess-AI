import chess
import chess.pgn
import re

class meth:
    def __init__(self):
        self.reg_parse = re.compile(r"(?:\w|\+|\#|\=|\-){2,6}(?=,|\))")
        self.piece_val = { 'P': 10, 'N': 25, 'B': 30, 'R': 50, 'Q': 100, 'K': 1000, 'p': -10, 'n': -25, 'b': -30, 'r': -50, 'q': -100, 'k': -1000}
        self.loc_val = {
            'P' : (
                1,  1,  1,  1,  1,  1,  1,  1,
                2,  2,  2,  3,  3,  2,  2,  2,
                2,  2,  3,  4,  4,  3,  2,  2,
                3,  3,  4,  5,  5,  4,  3,  3,
                3,  3,  4,  5,  5,  4,  3,  3,
                2,  2,  3,  4,  4,  3,  2,  2,
                10, 10, 10, 10, 10, 10, 10, 10,
                69, 69, 69, 69, 69, 69, 69, 69, 
            ),
            'N' : (
                 1,	1,	1,	1,	1,	1,	1,	1,
                2,	2,	2,	3,	3,	2,	2,	2,
                2,	2,	3,	4,	4,	3,	2,	2,
                3,	3,	4,	5,	5,	4,	3,	3,
                3,	3,	4,	5,	5,	4,	3,	3,
                2,	2,	3,	4,	4,	3,	2,	2,
                2,	2,	2,	3,	3,	2,	2,	2,
                1,	1,	1,	1,	1,	1,	1,	1, 
            ), 
           'B' : (
                1,	1,	1,	1,	1,	1,	1,	1,
                2,	2,	2,	3,	3,	2,	2,	2,
                2,	2,	3,	4,	4,	3,	2,	2,
                3,	3,	4,	5,	5,	4,	3,	3,
                3,	3,	4,	5,	5,	4,	3,	3,
                2,	2,	3,	4,	4,	3,	2,	2,
                2,	2,	2,	3,	3,	2,	2,	2,
                1,	1,	1,	1,	1,	1,	1,	1, 
            ),
            'R' : (
                1,	1,	1,	1,	1,	1,	1,	1,
                2,	2,	2,	3,	3,	2,	2,	2,
                2,	2,	3,	4,	4,	3,	2,	2,
                3,	3,	4,	5,	5,	4,	3,	3,
                3,	3,	4,	5,	5,	4,	3,	3,
                2,	2,	3,	4,	4,	3,	2,	2,
                2,	2,	2,	3,	3,	2,	2,	2,
                1,	1,	1,	1,	1,	1,	1,	1, 
            ),
            'Q' : (
                1,	1,	1,	1,	1,	1,	1,	1,
                2,	2,	2,	3,	3,	2,	2,	2,
                2,	2,	3,	4,	4,	3,	2,	2,
                3,	3,	4,	5,	5,	4,	3,	3,
                3,	3,	4,	5,	5,	4,	3,	3,
                2,	2,	3,	4,	4,	3,	2,	2,
                2,	2,	2,	3,	3,	2,	2,	2,
                1,	1,	1,	1,	1,	1,	1,	1, 
            ),
            'K' : (
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
            ),
        }

    def legal_move_list(self,board):
        """
        Get a list of legal moves in san notation
        """
        leg_move = board.legal_moves
        leg_move_list = re.findall(self.reg_parse,str(leg_move))
        return leg_move_list

    def board_value(self,board,player_col):
        """
        Evaluate the board position to good bad number

        player_col:
            WHITE = 1
            BLACK = -1
        """
        value = 0
        pmap = board.piece_map()
        for key in pmap:
            peice = pmap[key]
            value += self.piece_val[peice.symbol()]*player_col
            if peice.color and player_col == 1:
                value += self.loc_val[peice.symbol()][key]
            elif not(peice.color) and player_col == -1:
                value += self.loc_val[peice.symbol().capitalize()][63-key]

        return value
    
        
    def grow_twigs(self,board,player_col):
        """Returns tree from player col"""
        root = chess.pgn.Game()
        root.setup(board.fen())
        movelist = self.legal_move_list(board)
        # movespace = []
        for item in movelist:
            child = chess.pgn.GameNode()
            child.parent = root
            child.move = board.parse_san(item)
            score = self.board_value(child.board(),player_col)
            child.comment = [child.move, score]
            root.variations.append(child)
        return root
    
    def tree2(self,board,player_col):
        root = self.grow_twigs(board,player_col)
        test_space = []
        for cur in root.variations:
            child = self.grow_twigs(cur.board(),-player_col)
            for item in child.variations:
                test_space.append([cur.comment[0], cur.comment[1] - item.comment[1]])
        return test_space

    def tree3(self,board,player_col):
        root = self.grow_twigs(board,player_col)
        tree_space = []
        for cur1 in root.variations:
            child1 = self.grow_twigs(cur.board(),-player_col)
            for cur2 in child1.variations:
                child_2 = tree_space.append([cur1.comment[0], cur.comment[1]])

    # def recusive_tree(self,board,player_col,depth,depthlim):
    #     root = chess.pgn.Game()
    #     root.setup(board.fen())
    #     movelist = self.legal_move_list(board)
    #     # movespace = []
    #     for item in movelist:
    #         child = chess.pgn.GameNode()
    #         child.parent = root
    #         child.move = board.parse_san(item)
    #         score = self.board_value(child.board(),player_col)
    #         child.comment = [child.move, score]
    #         root.variations.append(child)

    #     if depth >= depthlim:9
    #         return root
    #     else:
    #         self.recursive_tree(board,-player_col,depth+1,depthlim)

        


    # def child_from_root(self,root,move):
    #     """generates a child from a root and a move"""
    #     child = chess.pgn.GameNode()
    #     child.parent = root
    #     child.move = board.parse_san(item)
    #     # score = self.help.board_value(child.board(),player_col)
    #     # child.comment = [child.move, score]
    #     return child

            

