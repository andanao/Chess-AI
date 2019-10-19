import chess
import chess.engine
import chess.pgn

# engine = chess.engine.SimpleEngine.popen_uci("C:\\Users\\Adrian\\Downloads\\stockfish-10-win\\stockfish-10-win\\Windows\\stockfish_10_x64")

# board = chess.Board()
# while not board.is_game_over():
#     result = engine.play(board, chess.engine.Limit(time=0.100))
#     board.push(result.move)

# engine.quit()


board  = chess.Board()
board.legal_moves 

chess.Move.from_uci("a8a1") in board.legal_moves


board.push_san("e4")

board.push_san("e5")

board.push_san("Qh5")

board.push_san("Nc6")

board.push_san("Bc4")

board.push_san("Nf6")

board.push_san("Qxf7")

board.is_checkmate()

print(board)