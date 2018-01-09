import unittest
from solution12 import Village
from solution12 import Program

class Solution12Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.example = Village('example_input.txt')
        self.puzzle = Village('puzzle_input.txt')
    
    def testExample01(self):
        self.assertEqual(self.example.get_network(0), [0, 2, 3, 4, 5, 6])
        
    def testExample02(self):
        self.assertEqual(self.example.get_network(1), [1])

    def testPuzzle01(self):
        self.assertEqual(len(self.puzzle.get_network(0)), 145)
        
    def testExample03(self):
        self.assertEqual(self.example.n_groups(), 2)

    def testPuzzle02(self):
        self.assertEqual(self.puzzle.n_groups(), 207)

if __name__ == '__main__':
    unittest.main()
    # v = Village('example_input.txt')
    # print(v.n_groups())