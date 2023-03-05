import random

class TicTacToe:
    def __init__(self):
        """Initializes the game
        Attributes:
            board (list): A list of 9 spaces representing the board
            player (str): The current player
            winning_combinations (list): A list of all the winning combinations as tuples"""
        # Fills the board with spaces and sets the player to X
        self.board = [' '] * 9
        self.player = 'X'
        self.winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
    

    def display_board(self):
        """Displays the board"""
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        

    def is_winner(self, player):
        """Checks if the current player has won"""
        for combo in self.winning_combinations:
            # Checks if the player has the same symbol in all the positions of any winning combinations
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == player:
                return True
        return False
    

    def is_tie(self):
        """Checks if the game is a tie"""
        for space in self.board:
            # Checks if there is any empty space left on the board technically meaning the game is not a tie but some games can be drawn before the board is full
            if space == ' ':
                return False
        return True
    

    def is_game_over(self):
        """Checks if the game is over"""
        return self.is_winner('X') or self.is_winner('O')
    
    def make_move(self, index):
        """Makes a move for the current player"""
        if self.board[index] == ' ':
            # this action may end the game so another check is needed
            self.board[index] = self.player
            
            # if the game is over the player does not change (otherwise the win is attributed to the other player)  
            if not self.is_game_over():
                # turns are switched
                if self.player == 'O':
                    self.player = 'X'
                else:
                    self.player = 'O' 
            return True
        else:
            return False
        

    """this will be changed to a monte carlo algorithm later""" 

    def get_computer_move(self):
        """Gets a random move for the computer"""
        possible_moves = []
        for index, space in enumerate(self.board):
            if space == ' ':
                possible_moves.append(index)
        return random.choice(possible_moves)
    
    
    def play(self):
        """Main game loop"""
        while True:
            self.display_board()
            if self.is_game_over():
                print(f"{self.player} wins!")
                break
            elif self.is_tie():
                print("Tie!")
                break
            else:
                # The player is asked for a move if it is their turn
                if self.player == 'X':
                    # minus 1 because the board is 0 indexed
                    move = int(input("Enter a number from 1 to 9: ")) - 1
                    while not self.make_move(move):
                        # if the move is invalid the player is asked to try again
                        move = int(input("Enter a number from 1 to 9: ")) - 1
                else:
                    # the computer makes a move
                    print("Computer's turn...")
                    move = self.get_computer_move()
                    self.make_move(move)



if __name__ == "__main__":
    game = TicTacToe()
    game.play()
    


    

