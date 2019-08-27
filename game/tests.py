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

    def test_check_winner(self):
        #game.show_board(self.boardComputerWin)
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
        move = game.get_random_move(self.boardFree,[0, 2, 6, 8])
        game.make_move(self.boardFree, self.computer, move)
        self.assertEqual(self.boardFree[move],self.computer)

    def test_check_space_free(self):
        move = game.get_random_move(self.boardFree,[0, 2, 6, 8])
        free = game.check_space_free(self.boardFree,move)
        move = game.get_random_move(self.boardFree,[0, 2, 6, 8])   
        full = game.check_space_free(self.boardFull,move)
        self.assertTrue(free)
        self.assertFalse(full)


    def test_check_board_full(self):
        free = game.check_board_full(self.boardFree)
        full = game.check_board_full(self.boardFull)
        self.assertFalse(free)
        self.assertTrue(full)
        pass

    def test_make_random_move(self):
        move = game.get_random_move(self.boardFull,[])
        self.assertEqual(move, None)
        move = game.get_random_move(self.boardFull,[0,2,6,8])
        self.assertEqual(move, None)

    def test_get_computer_move(self):
        move = game.get_computer_move(self.boardGame, self.computer)
        game.make_move(self.boardGame,self.computer,move)
        self.assertEqual(move,4)
        self.assertEqual(self.boardGame[move],self.computer)
