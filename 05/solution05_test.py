import unittest
import solution05

class Solution05Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.foo = 'bar'

    def testExample1(self):
        result = solution05.solve_maze_p1('example_input.txt')
        self.assertEqual(result[0], 5)
        self.assertEqual(result[1], [2, 5, 0, 1, -2])

    def testPuzzle1(self):
        result = solution05.solve_maze_p1('puzzle_input.txt')
        self.assertEqual(result[0], 375042)
    
    def testExample2(self):
        result = solution05.solve_maze_p2('example_input.txt')
        self.assertEqual(result[0], 10)
        self.assertEqual(result[1], [2, 3, 2, 3, -1])

    def testPuzzle2(self):
        result = solution05.solve_maze_p2('puzzle_input.txt')
        self.assertEqual(result[0], -1)

if __name__ == '__main__':
    unittest.main()
