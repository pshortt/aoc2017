import unittest
from day18 import solve_part1, solve_part2

class TestSolveDay18(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    def test_example01(self):
        self.assertEqual(solve_part1('day18/example1.input'), 4)

    def test_puzzle01(self):
        self.assertEqual(solve_part1('day18/puzzle.input'), 9423)

    def test_example02(self):
        self.assertEqual(solve_part2('day18/example2.input'), 3)

    def test_puzzle02(self):
        self.assertEqual(solve_part2('day18/puzzle.input'), 7620)
        
if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass