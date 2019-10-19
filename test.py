import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci("/usr/bin/stockfish")

board = chess.Board()
while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(time=0.100))
    board.push(result.move)

engine.quit()