fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'

piece_val = { 'P': 10, 'N': 25, 'B': 30, 'R': 50, 'Q': 100, 'K': 1000, 'p': -10, 'n': -25, 'b': -30, 'r': -50, 'q': -100, 'k': -1000}

val = 0
for peice in piece_val:
    val += fen.count(peice)*piece_val[peice]


print