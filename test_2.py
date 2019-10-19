import chess
import chess.pgn

game = chess.pgn.Game()
game.headers["Event"] = "Example"
node = game.add_variation(chess.Move.from_uci("e2e4"))
node = node.add_variation(chess.Move.from_uci("e7e5"))

node = node.add_variation(chess.Move.from_uci("g2g4"))
# node = node.add_variation(chess.Move.from_uci("Qh5"))
# node = node.add_variation(chess.Move.from_uci("Nc6"))
# node = node.add_variation(chess.Move.from_uci("Bc4"))
# node = node.add_variation(chess.Move.from_uci("Nf6"))
# node = node.add_variation(chess.Move.from_uci("Qxf7"))


node.comment = "Comment"

print(game)
print(game, file=open("test.pgn", "w+"), end="\n\n")