import os
import time
from colorama import Fore, Style, init

# Initialize colors
init()

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.player1_name = ""
        self.player2_name = ""
        self.player1_score = 0
        self.player2_score = 0
        
    def get_player_names(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN + "=== Welcome to Tic Tac Toe ===" + Style.RESET_ALL)
        self.player1_name = input("\nEnter first player's name (X): ")
        self.player2_name = input("Enter second player's name (O): ")

    def display_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n{self.player1_name}: {self.player1_score} | {self.player2_name}: {self.player2_score}\n")
        
        for i in range(0, 9, 3):
            print("\t     |     |")
            print("\t  {}  |  {}  |  {}".format(
                self._colorize(self.board[i]),
                self._colorize(self.board[i+1]),
                self._colorize(self.board[i+2])
            ))
            if i < 6:
                print("\t_____|_____|_____")
            else:
                print("\t     |     |")

    def _colorize(self, symbol):
        if symbol == "X":
            return Fore.RED + symbol + Style.RESET_ALL
        elif symbol == "O":
            return Fore.GREEN + symbol + Style.RESET_ALL
        return symbol

    def make_move(self, position, symbol):
        if self.board[position-1] == " ":
            self.board[position-1] = symbol
            return True
        return False

    def check_winner(self):
        # All winning combinations
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]  # Diagonal
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " "):
                return self.board[combo[0]]
        
        if " " not in self.board:
            return "Tie"
        
        return None

    def play_game(self):
        self.get_player_names()
        
        while True:
            self.board = [" " for _ in range(9)]
            current_player = "X"
            game_over = False
            
            while not game_over:
                self.display_board()
                player_name = self.player1_name if current_player == "X" else self.player2_name
                
                try:
                    position = int(input(f"\n{player_name} ({current_player}), choose a number between 1-9: "))
                    if position < 1 or position > 9:
                        print("Please enter a number between 1 and 9!")
                        time.sleep(1)
                        continue
                except ValueError:
                    print("Please enter a valid number!")
                    time.sleep(1)
                    continue

                if self.make_move(position, current_player):
                    winner = self.check_winner()
                    if winner:
                        self.display_board()
                        if winner == "Tie":
                            print("\nGame is a Tie!")
                        else:
                            winner_name = self.player1_name if winner == "X" else self.player2_name
                            print(f"\n🎉 Congratulations! {winner_name} has won! 🎉")
                            if winner == "X":
                                self.player1_score += 1
                            else:
                                self.player2_score += 1
                        game_over = True
                    else:
                        current_player = "O" if current_player == "X" else "X"
                else:
                    print("That position is already taken!")
                    time.sleep(1)

            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again != 'yes' and play_again != 'y':
                print("\nThanks for playing! 👋")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game() 