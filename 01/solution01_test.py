import unittest
import solution01

class TestSolveCaptcha(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        f = open('puzzle_input.txt', 'r')
        self.puzzle = f.read()
        f.close()

    def test_example_01(self):
        self.assertEquals(solution01.solve_captcha(1122), 3)
    
    def test_example_02(self):
        self.assertEquals(solution01.solve_captcha(1111), 4)    
    
    def test_example_03(self):
        self.assertEquals(solution01.solve_captcha(1234), 0)
        
    def test_example_04(self):
        self.assertEquals(solution01.solve_captcha(91212129), 9)

    def test_puzzle_input01(self):
        self.assertEquals(solution01.solve_captcha(self.puzzle), 1141)
        
    def test_example_05(self):
        self.assertEquals(solution01.solve_captcha2(1212), 6)
    
    def test_example_06(self):
        self.assertEquals(solution01.solve_captcha2(1221), 0)    
    
    def test_example_07(self):
        self.assertEquals(solution01.solve_captcha2(123425), 4)
        
    def test_example_08(self):
        self.assertEquals(solution01.solve_captcha2(123123), 12)
    
    def test_example_09(self):
        self.assertEquals(solution01.solve_captcha2(12131415), 4)

    def test_puzzle_input01(self):
        self.assertEquals(solution01.solve_captcha2(self.puzzle), 950)
            
    
if __name__ == '__main__':
    unittest.main()