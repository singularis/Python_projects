import unittest
import main

class Testgame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = main.run_quess(answer, guess)
        self.assertTrue(result)


    def test_input_wrong_guess(self):
        answer = 5
        guess = 0
        result = main.run_quess(answer, guess)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        answer = 5
        guess = 12
        result = main.run_quess(answer, guess)
        self.assertFalse(result)

    def test_input_wrong_string(self):
        answer = 5
        guess = '12'
        result = main.run_quess(answer, guess)
        self.assertFalse(result)



if __name__ == '__main__':
    unittest.main()