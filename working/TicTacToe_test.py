#!/usr/bin/env python3

from IPython.display import clear_output
from IPython import get_ipython
import sys

class TicTacToe:
    """Tic-Tac-Toe class. This class incorporates all the functions 
    to play the famous tic-tac-toe game between two players"""

    def __init__(self):
        """Class constructor. Initialize the basic elements"""
           
        self.move = {f's{i}':"" for i in range(1,10)}
        self.board = """
 {s1:^3} | {s2:^3} | {s3:^3}       1   2   3
-----+-----+-----
 {s4:^3} | {s5:^3} | {s6:^3}       4   5   6
-----+-----+-----      
 {s7:^3} | {s8:^3} | {s9:^3}       7   8   9       
                         
"""
        self.wins = {'Player 1':0, 'Player 2':0, 'Draw':0}
        self.env = self.check_running_env()


    def check_running_env(self):
        """Check if the code is running in a Jupyter notebook or in a terminal"""
        try:
            if get_ipython().__class__.__name__ == 'ZMQInteractiveShell':
                return 'notebook'
            else:
                return 'terminal'
        except NameError:
            return 'terminal'
        
        
    def reset_board(self):
        """Reset the board keeping the scoring"""
        self.move = {f's{i}':"" for i in range(1,10)}
        self.board = """
 {s1:^3} | {s2:^3} | {s3:^3}       1   2   3
-----+-----+-----
 {s4:^3} | {s5:^3} | {s6:^3}       4   5   6
-----+-----+-----      
 {s7:^3} | {s8:^3} | {s9:^3}       7   8   9       
                         
"""

        
    def show_board(self):
        """Display the current state of the board"""
        if self.env == 'notebook':
            clear_output()
            print("""\n 
        *******************
        *\033[1m Tic - Tac - Toe \033[0m*
        *******************
        \n""" + self.board.format(**self.move))
        
        elif self.env == 'terminal':
            text = '''\033[H\033[J\n 
            *******************
            *\033[1m Tic - Tac - Toe \033[0m*
            *******************\n
            ''' + self.board.format(**self.move)
            sys.stdout.write(text)
            sys.stdout.flush()


    def get_move(self, n, XO):
        """Ask the current player, n, to make a move -- make sure the square was not 
        already played.  XO is a string of the character (X or O) we will place in
        the desired square """
        valid_move = False
        while not valid_move:
            move = input(f'Player {n}, enter your move (1-9) (or q to quit): ')
            if 'q' in move:
                raise KeyboardInterrupt
            try: 
                if int(move) in range(1, 10) and self.move[f's{move}'] == "":
                    valid_move = True
                else:
                    print(f'Invalid move: {self.move[f"s{move}"]}')
            except ValueError:
                print('Please, enter a valid move')
              
        self.move[f's{move}'] = XO


    def check_winner(self):
        """Check for winning conditions. This function checks the board looking for three identical symbols
        on the same row, column or diagonal"""
        win = False
        winner = None
        symb2player = lambda s : 1 if(s == 'X') else 2
        for i in [1, 2, 3]:
            if self.move[f's{i}'] == self.move[f's{i+3}'] == self.move[f's{i+6}'] != '':
                win = True
                winner = symb2player(self.move[f's{i}'])
                
        for i in [1, 4, 7]:
            if self.move[f's{i}'] == self.move[f's{i+1}'] == self.move[f's{i+2}'] != '':
                win = True
                winner = symb2player(self.move[f's{i}'])
                
        if self.move[f's{1}'] == self.move[f's{5}'] == self.move[f's{9}'] != '':
                win = True
                winner = symb2player(self.move[f's{5}'])
            
        if self.move[f's{3}'] == self.move[f's{5}'] == self.move[f's{7}'] != '':
                win = True
                winner = symb2player(self.move[f's{5}'])
            
        return win, winner     


    def play_a_game(self):
        """Play a single game of tic-tac-toe """
        rand_start = input('Start the game with a random player (y/n): ')
        if 'y' in rand_start:
            player = {1,2}.pop()
        else:
            player = input('Insert starting player (1 or 2): ')
            if player not in ['1', '2']: 
                player = input('Please insert a valid starting player (1 or 2): ')

        self.show_board()
    
        while '' in self.move.values():
            if player == 1: XO = 'X'
            else: XO = 'O'
            try:
                self.get_move(player, XO)
            except KeyboardInterrupt:
                break
            self.show_board()
            player = ({1,2} - {player}).pop()
            win, winner = self.check_winner()
            if win:
                self.wins[f'Player {winner}'] += 1
                print(f'Congrats player {winner}, you are the winner!')
                return winner
            
        self.wins['Draw'] += 1
        print('Draw')
        

    def score(self):
        """Display the current score"""
        print(f"""
----------------------
Player 1 | {self.wins['Player 1']}
----------------------
Player 2 | {self.wins['Player 2']}
----------------------
Draw     | {self.wins['Draw']}
----------------------
""")
        

    def play(self):
        """Play Tic - Tac - Toe"""
        
        print("""\n 
        *******************
        *\033[1m Tic - Tac - Toe \033[0m*
        *******************
        \n""")

        want2play = True

        while want2play:
            game = self.play_a_game()
            self.reset_board()
            
            if input('See score (y/n)? ') == 'y':
                self.score()
            
            if input('Play again (y/n)? ') == 'n':
                want2play = False
                
        print('\n\n\033[1mFinal score \033[0m')
        self.score()
            
            
        
        
if __name__ == '__main__':
    game = TicTacToe()
    game.play()