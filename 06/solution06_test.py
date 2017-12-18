import unittest
import solution06

class Solution06Test(unittest.TestCase):        
    def testExample01(self):
        result = solution06.RedistInfLoopCheck([0,2,7,0])
        self.assertEqual(result.ctr, 5)
        
    def testExample02(self):
        result = solution06.RedistInfLoopCheck([0,2,7,0])
        self.assertEqual(result.ncycles, 4)
        
    def testIterateBanks(self):
        self.assertEqual(solution06.iterate_banks([0,2,7,0]), [2,4,1,2])
        
    def testPuzzle01(self):
        result = solution06.RedistInfLoopCheck([11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11])
        self.assertEqual(result.ctr, 4074)
        
    def testPuzzle01(self):
        result = solution06.RedistInfLoopCheck([11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11])
        self.assertEqual(result.ncycles, 2793)

if __name__ == '__main__':
    unittest.main()
