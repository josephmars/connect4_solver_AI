from connect4 import *
import random

def ai_vs_ai(algorithm_ai1 = "minimax", depth_ai1 = 1, algorithm_ai2= "alpha-beta", depth_ai2 = 1):
    game = ConnectFour()
    winner = "draw"
    while True:
        # Switch information to make the AI1 play as player 2 (randomly with 50% chance)
        if random.random() < 0.5:
            algorithm_ai1, algorithm_ai2 = algorithm_ai2, algorithm_ai1
            depth_ai1, depth_ai2 = depth_ai2, depth_ai1
        
        # AI1's turn
        if algorithm_ai1 == "minimax":
            ai1_move = minimax(game, depth = depth_ai1)
        elif algorithm_ai1 == "alpha-beta":
            ai1_move = alpha_beta_pruning(game, depth = depth_ai1)
        game.make_move(ai1_move)

        if game.is_winner(1):
            winner = algorithm_ai1
            break
        elif game.is_board_full():
            break

        # AI2's turn
        if algorithm_ai2 == "minimax":
            ai2_move = minimax(game, depth = depth_ai2)
        elif algorithm_ai2 == "alpha-beta":
            ai2_move = alpha_beta_pruning(game, depth = depth_ai2)
        game.make_move(ai2_move)
        
        if game.is_winner(-1):
            winner = algorithm_ai2
            break
        elif game.is_board_full():
            break
        
    return {"winner": winner, "player1": algorithm_ai1}
        