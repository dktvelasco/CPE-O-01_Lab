''' This is the main logic for a Tic-tac-toe game.
It is not optimised for a quality game it simply
generates random moves and checks the results of
a move for a winning line. Exposed functions are:
__init__()
saveGame()
restoreGame()
userMove()
computerMove()
'''

import os, random
import oxo_data


class Game:
    def __init__(self):
        self.board = [" "]*9

    def saveGame(self):
        ' save game to disk '
        oxo_data.saveGame(self.board)
        
    def restoreGame(self):
        ''' restore previously saved game.
        If game not restored successfully return new game'''
        try:
            game = oxo_data.restoreGame()
            if len(game) == 9:
                self.board = game
            else: self.board = [" "]*9
        except IOError:
            self.board = [" "]*9

   def _generateMove(game):
        ''' generate a random cell from thiose available.
            If all cells are used return -1'''
        options = [i for i in range(len(game)) if  game[i] == " "]
        if options:
            return random.choice(options)
        else: return -1
        
    def _isWinningMove(self, player):
        wins = ((0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6))

        for a,b,c in wins:
            chars = self.board[a] + self.board[b] + self.board[c]
            if chars == player*3:
                return True
        return False

    def userMove(self,cell):
        if self.board[cell] != ' ':
            raise ValueError('Invalid cell')
        else:
            self.board[cell] = 'X'
        if self.isWinningMove('X'):
            return 'X'
        else:
            return ""

    def computerMove(self):
        cell = self.generateMove()
        if cell == -1:
            return 'D'
        self.board[cell] = 'O'
        if self.isWinningMove('O'):
            return 'O'
        else:
            return ""

    def test(self):
        result = ""
        while not result:
            print(self)
            try:
                cell = int(input("Make your move: "))
                result = self.userMove(cell)
            except (ValueError, IndexError):
                print("Oops, that shouldn't happen")
            if not result:
                result = self.computerMove()
                
            if not result: continue
            elif result == 'D':
                print("Its a draw")
            else:
                print("Winner is:", result)
            print(self.board)

if __name__ == "__main__":
    game = Game()
    game.test()
    game.saveGame()
