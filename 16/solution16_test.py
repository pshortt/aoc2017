import unittest
from solution16 import run_dance, run_dance_x, memoize_dance

class Solution16Test(unittest.TestCase):
    def testExample01(self):
        self.assertEqual(run_dance('example_input.txt', 'abcde'), 'baedc')

    def testPuzzle01(self):
        self.assertEqual(run_dance('puzzle_input.txt', 'abcdefghijklmnop'), 'jcobhadfnmpkglie')
       
    def testExample02(self):
        self.assertEqual(run_dance_x('example_input.txt', 'abcde', 1000000000), 'abcde')

    def testPuzzle02(self):
        self.assertEqual(run_dance_x('puzzle_input.txt', 'abcdefghijklmnop', 1000000000), 'pclhmengojfdkaib')

if __name__ == '__main__':
    unittest.main()
    
    # for s in memoize_dance('puzzle_input.txt', 'jcobhadfnmpkglie'):
        # print(s)
    # print('----------------')
    # print(run_dance_x('puzzle_input.txt', 'jcobhadfnmpkglie', 1))
    # print(run_dance_x('puzzle_input.txt', 'jcobhadfnmpkglie', 60))
    # print(run_dance_x('puzzle_input.txt', 'jcobhadfnmpkglie', 61))