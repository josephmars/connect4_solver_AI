from connect4 import *

if __name__ == "__main__":
    game = ConnectFour()
    
    player = int(input("Choose player (1 or 2): "))
    if player == 2:
        # AI's turn
        print("AI is thinking...")
        ai_move = minimax(game, depth = 4)  # Choose algorithm: "minimax" or "alpha-beta", and depth
        print(f"AI plays in column {ai_move+1}")
        game.make_move(ai_move)
        

    while True:
        game.display_board()
        col = int(input("Enter your move (1-7): "))
        if game.is_valid_move(col-1):
            game.make_move(col-1)
            game.display_board()
            if game.is_winner(1):
                print("Player 1 wins!")
                break
            if game.is_winner(-1):
                print("Player 2 wins!")
                game.display_board()
                break
            elif game.is_board_full():
                print("It's a draw!")
                break
            
            # AI's turn
            print("AI is thinking...")
            ai_move = minimax(game,depth = 4)  # Choose algorithm: "minimax" or "alpha-beta"
            print(f"AI plays in column {ai_move+1}")
            game.make_move(ai_move)
            if game.is_winner(1):
                print("Player 1 wins!")
                break
            if game.is_winner(-1):
                print("Player 2 wins!")
                game.display_board()
                break
            elif game.is_board_full():
                print("It's a draw!")
                game.display_board()
                break
        else:
            print("Invalid move. Try again.")