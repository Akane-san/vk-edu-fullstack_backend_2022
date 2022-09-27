import unittest
from tictac_game import TicTacGame


# Test cases to test Calulator methods
# You always create  a child class derived from unittest.TestCase
class TestTicTacGamer(unittest.TestCase):

    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.tictac_game = TicTacGame()

    # Each test method starts with the keyword test_
    def test_validate_wrong_input(self):
        with self.assertRaises(ValueError):
            self.tictac_game.validate_input("")
        with self.assertRaises(ValueError):
            self.tictac_game.validate_input("1")
        with self.assertRaises(ValueError):
            self.tictac_game.validate_input("a")
        with self.assertRaises(ValueError):
            self.tictac_game.validate_input("a 1")
        with self.assertRaises(ValueError):
            self.tictac_game.validate_input("4 1")
        with self.assertRaises(ValueError):
            self.tictac_game.validate_input("1 2 3")

    def test_validate_right_input(self):
        self.assertIsNone(self.tictac_game.validate_input("1 2"))

    def test_check_winner(self):
        for i in range(3):
            for j in range(3):
                self.tictac_game.board[i][j] = 'X'
        self.assertEqual(self.tictac_game.check_winner('X'), True)
        self.assertEqual(self.tictac_game.check_winner('O'), False)

    def test_check_line(self):
        self.assertEqual(self.tictac_game.check_line('X', 'X', 'X', 'X'), True)
        self.assertEqual(self.tictac_game.check_line('X', 'O', 'X', 'X'), False)


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
