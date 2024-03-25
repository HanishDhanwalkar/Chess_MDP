# print(board)

# print(board.legal_moves)

# board.push_san("e4")
# board.pop() 

# print(board)


import asyncio
import chess
import chess.engine

async def main() -> None:
    transport, engine = await chess.engine.popen_uci('stockfish-windows-x86-64\stockfish\stockfish-windows-x86-64.exe')

    board = chess.Board()
    while not board.is_game_over():
        result = await engine.play(board, chess.engine.Limit(time=0.1))
        board.push(result.move)
        print(board, "\n ---------------------------------------------------------")
    await engine.quit()

    print(board)

asyncio.run(main())