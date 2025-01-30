import numpy as np

from copy import deepcopy
class ConnectFour:
    def __init__(self):
        self.board = np.zeros((6, 7), dtype=int)
        self.player = 1  # 1 for player 1, -1 for player 2

    def display_board(self):
        print(self.board)

    def is_valid_move(self, col):
        return self.board[0][col] == 0

    def make_move(self, col):
        for row in range(5, -1, -1):
            if self.board[row][col] == 0:
                self.board[row][col] = self.player
                break
        
        self.switch_player()

    def switch_player(self):
        self.player = -self.player

    def is_winner(self, player):
        # Check horizontally
        for row in range(6):
            for col in range(4):
                if all(self.board[row][col + i] == player for i in range(4)):
                    return True

        # Check vertically
        for col in range(7):
            for row in range(3):
                if all(self.board[row + i][col] == player for i in range(4)):
                    return True

        # Check diagonally (from bottom-left to top-right)
        for row in range(3, 6):
            for col in range(4):
                if all(self.board[row - i][col + i] == player for i in range(4)):
                    return True

        # Check diagonally (from top-left to bottom-right)
        for row in range(3):
            for col in range(4):
                if all(self.board[row + i][col + i] == player for i in range(4)):
                    return True

        return False

    def is_board_full(self):
        return not any(self.board[0][col] == 0 for col in range(7))

def evaluate_board(board):
    """Evaluation function: sum(i^2*p1[i] - i^2*p2[i]) + 1000*p1[4] - 1000*p2[4] with i = 1,2,3.
    p1_i is the number of lines of i discs of player 1, p2_i is the number of lines of i discs of player 2.
    the +-1000 are for winning/losing.

    Args:
        board (np.array): 6x7 board
    """
    p1 = [0, 0, 0, 0]
    p2 = [0, 0, 0, 0]
    
    # Check horizontally
    for row in range(6):
        for col in range(4):
            if all(board[row][col + i] == 1 for i in range(4)):
                p1[3] += 1
            elif all(board[row][col + i] == -1 for i in range(4)):
                p2[3] += 1
            elif all(board[row][col + i] == 1 for i in range(3)):
                p1[2] += 1
            elif all(board[row][col + i] == -1 for i in range(3)):
                p2[2] += 1
            elif all(board[row][col + i] == 1 for i in range(2)):
                p1[1] += 1
            elif all(board[row][col + i] == -1 for i in range(2)):
                p2[1] += 1
            elif board[row][col] == 1:
                p1[0] += 1
            elif board[row][col] == -1:
                p2[0] += 1
                
    # Check vertically
    for col in range(7):
        for row in range(3):
            if all(board[row + i][col] == 1 for i in range(4)):
                p1[3] += 1
            elif all(board[row + i][col] == -1 for i in range(4)):
                p2[3] += 1
            elif all(board[row + i][col] == 1 for i in range(3)):
                p1[2] += 1
            elif all(board[row + i][col] == -1 for i in range(3)):
                p2[2] += 1
            elif all(board[row + i][col] == 1 for i in range(2)):
                p1[1] += 1
            elif all(board[row + i][col] == -1 for i in range(2)):
                p2[1] += 1
            elif board[row][col] == 1:
                p1[0] += 1
            elif board[row][col] == -1:
                p2[0] += 1
    
    # Check diagonally (from bottom-left to top-right)
    for row in range(3, 6):
        for col in range(4):
            if all(board[row - i][col + i] == 1 for i in range(4)):
                p1[3] += 1
            elif all(board[row - i][col + i] == -1 for i in range(4)):
                p2[3] += 1
            elif all(board[row - i][col + i] == 1 for i in range(3)):
                p1[2] += 1
            elif all(board[row - i][col + i] == -1 for i in range(3)):
                p2[2] += 1
            elif all(board[row - i][col + i] == 1 for i in range(2)):
                p1[1] += 1
            elif all(board[row - i][col + i] == -1 for i in range(2)):
                p2[1] += 1
            elif board[row][col] == 1:
                p1[0] += 1
            elif board[row][col] == -1:
                p2[0] += 1
    
    # Check diagonally (from top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            if all(board[row + i][col + i] == 1 for i in range(4)):
                p1[3] += 1
            elif all(board[row + i][col + i] == -1 for i in range(4)):
                p2[3] += 1
            elif all(board[row + i][col + i] == 1 for i in range(3)):
                p1[2] += 1
            elif all(board[row + i][col + i] == -1 for i in range(3)):
                p2[2] += 1
            elif all(board[row + i][col + i] == 1 for i in range(2)):
                p1[1] += 1
            elif all(board[row + i][col + i] == -1 for i in range(2)):
                p2[1] += 1
            elif board[row][col] == 1:
                p1[0] += 1
            elif board[row][col] == -1:
                p2[0] += 1
    
    total_score =  sum((i^2)*p1[i] - (i^2)*p2[i] for i in range(3)) + 1000*p1[3] - 1000*p2[3]
    return total_score
def sucessor_function(board, player):
    # returns a list of all possible boards that can be reached from the current board
    # by adding a disc in any of the columns that are not full
    boards = []
    for col in range(7):
        if board[0][col] == 0:
            new_board = deepcopy(board)
            for row in range(5, -1, -1):
                if new_board[row][col] == 0:
                    new_board[row][col] = player
                    break
            boards.append({'board': new_board, 'col': col})
    return boards
def create_state_tree(board, player, depth = 1):
    # returns a tree of all possible states that can be reached from the current board
    if player == 1:
        type_player = "max"
    else:
        type_player = "min"
        
    tree = [{"Id": 0, "node_depth":0, "score" : None, "board" : board, "move": None, "type": type_player, "parent_id" : None, "children":[]}]
    for i in range(depth):

        
        # for each node in the tree, add a new node for each possible move
        # get the last nodes added to the tree based on the node_depth
        last_nodes = [node for node in tree if node["node_depth"] == i]
        for node in last_nodes:
            # for each node, add a new node for each possible move of the player
            for next_move in sucessor_function(node["board"], player):
                
                if player == 1:
                    type_next_player = "min"
                else:
                    type_next_player = "max"
                
                # add the child node id to the parent node
                tree[node["Id"]]["children"].append(len(tree))
                
                # add the new node to the tree
                tree.append({"Id": len(tree), "node_depth":i+1, "score" : None, "board" : next_move["board"], "move": next_move["col"],"type": type_next_player, "parent_id" : node["Id"], "children":[]})
        
        # switch player
        player = -player
    
    return tree
def minimax(game, depth=1):
    # returns the column where the disc should be placed
    # based on the minimax algorithm
    # the algorithm is implemented using a tree of possible states that can be reached from the current board
    # the tree is created using the create_state_tree function
    # the evaluation function is evaluate_board
    tree = create_state_tree(game.board, game.player, depth)
    # go node by node and evaluate the board, starting from the leaves (last nodes added to the tree)
    for node in reversed(tree):
        if len(node["children"]) == 0:
            # if the node is a leaf, evaluate the board
            node["score"] = evaluate_board(node["board"])
        else:
            # if the node is not a leaf, evaluate the board based on the children nodes
            if node["type"] == "max":
                node["score"] = max([tree[child]["score"] for child in node["children"]])
            else:
                node["score"] = min([tree[child]["score"] for child in node["children"]])
    
    # get the optimal move based on the root node
    optimal_move = None
    for child in tree[0]["children"]:
        if tree[child]["score"] == tree[0]["score"]:
            optimal_move = tree[child]["move"]
            break
    
    return optimal_move
    
def alpha_beta(tree, node):
    # returns the score of the node
    # based on the alpha-beta pruning algorithm
    alpha = -np.inf
    beta = np.inf
    if len(node["children"]) == 0:
        # if the node is a leaf, evaluate the board
        return evaluate_board(node["board"])
    else:
        if node["type"] == "max":
            # print("node:", node)
            for child_id in node["children"]:
                alpha = max(alpha, alpha_beta(tree, tree[child_id]))
                if beta <= alpha:
                    break
            return alpha
        else:
            for child_id in node["children"]:
                beta = min(beta,alpha_beta(tree, tree[child_id]))
                if beta <= alpha:
                    break
            return beta
    
def alpha_beta_pruning(game, depth):
    # returns the column where the disc should be placed
    # based on the alpha-beta pruning algorithm
    board = game.board
    player = game.player
    tree = create_state_tree(board, player, depth)
    
    # get the optimal move based on the root node
    root_node = tree[0]
    score_root_node = alpha_beta(tree, root_node)
    optimal_move = None
    for child in root_node["children"]:
        if alpha_beta(tree, tree[child]) == score_root_node:
            optimal_move = tree[child]["move"]
            # print("optimal_move:", optimal_move)
    
    return optimal_move