import unittest
from solution11 import HexGridDist

class Solution11Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        f = open('puzzle_input.txt')
        self.puzzle = f.readline()
        f.close()
        
    def testExample01(self):
        res = HexGridDist('ne,ne,ne')
        self.assertEqual(res.min_steps, 3)

    def testExample02(self):
        res = HexGridDist('ne,ne,sw,sw')
        self.assertEqual(res.min_steps, 0)
    
    def testExample03(self):
        res = HexGridDist('ne,ne,s,s')
        self.assertEqual(res.min_steps, 2)

    def testExample04(self):
        res = HexGridDist('se,sw,se,sw,sw')
        self.assertEqual(res.min_steps, 3)

    def testPuzzle01(self):
        res = HexGridDist(self.puzzle)
        self.assertEqual(res.min_steps, 747)

    def testPuzzle02(self):
        res = HexGridDist(self.puzzle)
        self.assertEqual(res.max_hist_dist, 1544)
if __name__ == '__main__':
    unittest.main()
