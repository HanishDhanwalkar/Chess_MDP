import asyncio
import chess
import chess.engine

async def user_move(board):

    while True:
        try:
            user_input = input("Enter your move (in algebraic notation, e.g., e2e4): ")
            move = chess.Move.from_uci(user_input)
            if move in board.legal_moves:
                return move
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid move.")

async def main() -> None:
    # Adjust the path to the Stockfish executable based on your system
    engine_path = "stockfish-windows-x86-64\stockfish\stockfish-windows-x86-64.exe"
    transport, engine = await chess.engine.popen_uci(engine_path)

    board = chess.Board()
    while not board.is_game_over():
        if board.turn == chess.WHITE:  # Player's turn
            move = await user_move(board)
            board.push(move)
        else:  # Engine's turn
            result = await engine.play(board, chess.engine.Limit(time=0.1))
            board.push(result.move)
        
        print(board)
        print("---------------------------------------------------------")
    
    await engine.quit()

    print("Game Over:", board.result())

# Run the asyncio event loop with the main coroutine
asyncio.run(main())
