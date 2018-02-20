import unittest
from solution16 import run_dance

class Solution16Test(unittest.TestCase):
    def testExample01(self):
        self.assertEqual(run_dance('example_input.txt', 5), 'baedc')

    def testPuzzle01(self):
        self.assertEqual(run_dance('puzzle_input.txt'), None)

if __name__ == '__main__':
    unittest.main()
