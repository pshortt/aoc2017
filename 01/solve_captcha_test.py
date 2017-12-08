import unittest
import solution01

class TestSolveCaptcha(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.puzzle = open('puzzle_input.txt', 'r').read();

    def test_example_01(self):
        self.assertEquals(solution01.solve_captcha(1122), 3)
    
    def test_example_02(self):
        self.assertEquals(solution01.solve_captcha(1111), 4)    
    
    def test_example_03(self):
        self.assertEquals(solution01.solve_captcha(1234), 0)
        
    def test_example_04(self):
        self.assertEquals(solution01.solve_captcha(91212129), 9)
    
    def test_puzzle_input(self):
        self.assertEquals(solution01.solve_captcha(self.puzzle), 99)
        
if __name__ == '__main__':
    unittest.main()