"""
Author: Charles Ivan Matthew C. Nangit
Date: April 7, 2022
Filename: oxo_logic.py
Project Description: The class Game() is added to the current oxo_logic.py file
"""

import os, random
import oxo_data

class Game():
    def __init__(game):
        game.board = list (" " * 9)

    def newGame(game):
        ' return new empty game '
        return list(" " * 9)
    
    def saveGame(game, play):
        'safe game to disk '
        oxo_data.saveGame(game.board)

    def restoreGame(game):
        ''' restore previously saved game.
        If game not restored successfully return new game'''
        try:
            game.board = oxo_data.restoreGame()
            if len(game.board) == 9:
                game.board = list(" " * 9)
            return game.board
        except IOError:
            game.board = list(" " * 9)
            return game.board
    
    def _generateMove(game):
        ''' generate a random cell from thiose available.
            If all cells are used return -1'''
        options = [i for i in range(len(game.board)) if  game.board[i] == " "]
        if options:
            return random.choice(options)
        else: return -1

    def _isWinningMove(game):
        wins = ((0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6))
        game = game.board
        for a,b,c in wins:
            chars = game[a] + game[b] + game[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False

    def userMove(game, cell):
        if game.board[cell] != ' ':
            raise ValueError('Invalid cell')
        else:
            game.board[cell] = 'X'
        if game._isWinningMove():
            return 'X'
        else:
            return ""
    
    def computerMove(game):
        cell = game._generateMove()
        if cell == -1:
            return 'D'
        game.board[cell] = 'O'
        if game._isWinningMove():
            return 'O'
        else:
            return ""

def test():
    result = ""
    play = Game()
    while not result:
        print(play.board)
        try:
            result = play.userMove(play._generateMove())
        except ValueError:
            print("Oops, that shouldn't happen")
        if not result:
            result = play.computerMove()
            
        if not result: continue
        elif result == 'D':
            print("Its a draw")
        else:
            print("Winner is:", result)
        print(play.board)
    
if __name__ == "__main__":
    test()