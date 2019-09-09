import unittest
from . import tictactoe as game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.boardComputerWin = ['X', 'X', 'X', ' ', 'O', 'O', ' ', 'O', ' ']
        self.boardUserWin = ['O', ' ', 'X', 'O', ' ', 'O', 'O', ' ', ' ']
        self.boardFree = ['O', ' ', 'X', 'O', ' ', 'X', 'O', ' ', ' ']  
        self.boardFull = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
        self.boardGame = [' ']*9
        self.player = 'O'
        self.computer = 'X'

    def test_evaluate(self):
        result = game.evaluate(self.boardComputerWin)
        self.assertEqual(result, 1)
        result = game.evaluate(self.boardUserWin)
        self.assertEqual(result, -1)

    def test_get_free_spaces(self):
        free_spaces = game.get_free_spaces(self.boardFull)
        self.assertEqual(len(free_spaces),0)
        free_spaces = game.get_free_spaces(self.boardGame)
        self.assertEqual(len(free_spaces), 9)
        free_spaces = game.get_free_spaces(self.boardComputerWin)
        self.assertEqual(len(free_spaces), 3)

    def test_minimax(self):
        depth = len(game.get_free_spaces(self.boardComputerWin))
        move = game.minimax(self.boardComputerWin, depth, self.computer)
        self.assertEqual(1, move[1])
        depth = len(game.get_free_spaces(self.boardUserWin))
        move = game.minimax(self.boardUserWin,depth,self.player)
        self.assertEqual(-1, move[1])

    def test_check_winner(self):
        win_computer = game.check_winner(self.boardComputerWin,self.computer);
        win_user = game.check_winner(self.boardComputerWin, self.player);
        self.assertTrue(win_computer)
        self.assertFalse(win_user)

        #game.show_board(self.boardUserWin)
        win_computer = game.check_winner(self.boardUserWin, self.computer);
        win_user = game.check_winner(self.boardUserWin, self.player);
        self.assertFalse(win_computer)
        self.assertTrue(win_user)

    def test_make_move(self):
        move = game.get_computer_move(self.boardFree)
        game.make_move(self.boardFree, self.computer, move)
        self.assertEqual(self.boardFree[move],self.computer)

    def test_check_space_free(self):
        move = game.get_computer_move(self.boardFull)
        free = game.check_space_free(self.boardFree,move)
        move = game.get_computer_move(self.boardFree)
        full = game.check_space_free(self.boardFull,move)
        self.assertTrue(free)
        self.assertFalse(full)


    def test_check_board_full(self):
        free = game.check_board_full(self.boardFree)
        full = game.check_board_full(self.boardFull)
        self.assertFalse(free)
        self.assertTrue(full)
        pass

    def test_get_computer_move(self):
        move = game.get_computer_move(self.boardGame)
        game.make_move(self.boardGame,self.computer,move)
        self.assertEqual(move,0)
        self.assertEqual(self.boardGame[move],self.computer)
