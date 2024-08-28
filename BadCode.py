# play tictactoe randomly
import numpy as np

n_games = 100
results = []

for n in range(n_games):
    # player 1: 1
    # player 2: -1
    board = np.zeros((3, 3))

    player = 1
    done = False

    while not done:
        # get available spots
        available = []
        for i in range(3):
            for j in range(3):
                if board[i, j] == 0:
                    available.append((i, j))
        
        # choose random move
        move_idx = np.random.randint(low = 0, high=len(available))
        move = available[move_idx]
        board[move[0], move[1]] = player
        
        # check if a player won
        # check horizontal
        for i in range(3):
            s = sum(board[i, :])
            if abs(s) == 3:
                done = True
                results.append(player)
                print('Player ', player, 'won tictactoe')
                break
        
        # check vertical
        for j in range(3):
            s = sum(board[:, j])
            if abs(s) == 3:
                done = True
                results.append(player)
                print('Player ', player, 'won tictactoe')
                break
        
        # check diagonal
        s = board[0, 0] + board[1, 1] + board[2, 2]
        if abs(s) == 3:
            done = True
            results.append(player)
            print('Player ', player, 'won tictactoe')
            break
            
        s = board[2, 0] + board[1, 1] + board[0, 2]
        if abs(s) == 3:
            done = True
            results.append(player)
            print('Player ', player, 'won tictactoe')
            break
        
        # check for a tie
        s = np.sum(board == 0)
        if s == 0:
            done = True
            results.append(0)
            print("It's a tie!")
            break
        
        player = 1 if player == -1 else -1
        
print(results)