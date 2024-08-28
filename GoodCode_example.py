# play tictactoe randomly
import numpy as np


def check_available_moves(board: np.array) -> list:
    """Checks the board for available moves. If a place on the board is 0, then it is available. Else it is occupied by a player.

    Args:
        board (np.array): Numpy array representation of the tictactoe board

    Returns:
        list: A list with coordinates of available moves
    """
    # Check which coordinates have value 0.
    available = []
    for row in range(3):
        for col in range(3):
            if board[row, col] == 0:
                available.append((row, col))
    return available

def make_move(board: np.array, available: list, player: int) -> np.array:
    """Makes a move on the board, based on the available moves and the player who's turn it is

    Args:
        board (np.array): Numpy array representation of the tictactoe board
        available (list): A list with coordinates of available moves
        player (int): Who's turn it is

    Returns:
        np.array: the tictactoe board
    """
    move_idx = np.random.randint(low = 0, high=len(available))
    move = available[move_idx]
    board[move[0], move[1]] = player
    return board

def check_horizontal(board: np.array, player: int) -> tuple[bool, int]:
    # check horizontal
    for row in range(3):
        s = sum(board[row, :])
        done, winner = is_winner(s, player)
        if done:
            return done, winner
    return False, 0
        
def check_vertical(board: np.array, player: int) -> tuple[bool, int]:
    # check vertical
    for col in range(3):
        s = sum(board[:, col])
        done, winner = is_winner(s, player)
        if done:
            return done, winner
    return False, 0
        
def is_winner(s: int, player: int) -> tuple[bool, int]:
    """Check if there is a winner of the game. 

    Args:
        s (int): The sum of the horizontal/vertical/diagonal matrix
        player (int): Who's turn it is

    Returns:
        tuple[bool, int]: done, winner. Returns whether the game is over and if there is a winner
    """
    if abs(s) == 3:
        done = True
        winner = player
        print('Player', player, 'won tictactoe')
        return done, winner
    return False, 0

def check_winner(board: np.array, player: int) -> tuple[bool, int]:
    """Check if there is a winner of the game in any way

    Args:
        board (np.array):  Numpy array representation of the tictactoe board
        player (int): Who's turn it is

    Returns:
        tuple[bool, int]: done, winner. Returns whether the game is over and if there is a winner
    """
    done, winner = check_vertical(board, player)
    if done:
        return done, winner
    
    done, winner = check_horizontal(board, player)
    if done:
        return done, winner
    
    # check diagonal
    s = board[0, 0] + board[1, 1] + board[2, 2]
    done, winner = is_winner(s, player)
    if done:
        return done, winner
    
    s = board[2, 0] + board[1, 1] + board[0, 2]
    done, winner = is_winner(s, player)
    if done:
        return done, winner
    return False, 0
    

def play_tictactoe() -> int:
    """Plays 1 round of tic tac toe.

    Returns:
        int: The winner of the tic tac toe game. If it's 0, then it's a tie. 
    """
    # player 1: 1
    # player 2: -1
    player = 1
    
    board = np.zeros((3, 3))    
    winner = 0
    done = False

    while not done:
        # get available spots
        available = check_available_moves(board)
        
        # choose random move
        board = make_move(board, available, player)
        
        # check if a player won
        done, winner = check_winner(board, player)
        if done:
            return winner
        
        # check for a tie
        s = np.sum(board == 0) # count the number of 0s on the board. If it's 0, then all places are filled and it's a tie
        if s == 0:
            done = True
            winner = 0
            print("It's a tie!")
            return winner
        
        player = 1 if player == -1 else -1

def main(n_games: int) -> list:
    """The main function for running a tictactoe simulation where the moves are played randomly. 

    Args:
        n_games (int): the number of games that you want to simulate

    Returns:
        list: the results of all the games
    """
    results = []

    for n in range(n_games):
        winner = play_tictactoe()
        results.append(winner)
    return results

if __name__ == '__main__':
    n_games = 10000
    results = main(n_games)
    print(results)