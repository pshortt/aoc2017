import unittest
from solution15 import genseq, judge, count_judge

class Solution15Test(unittest.TestCase):
    # def testExample01(self):
        # self.assertEqual(count_judge(65, 8921), 588)
        
    # def testPuzzle01(self):
        # self.assertEqual(count_judge(516, 190), 597)
        
    def testExample02(self):
        self.assertEqual(count_judge(65, 8921, 5*10**6, 4, 8), 309)
        
    def testPuzzle02(self):
        self.assertEqual(count_judge(516, 190, 5*10**6, 4, 8), -1)
    
    def testGenseq01(self):
        self.assertEqual(genseq(65, 16807, 5), [1092455, 1181022009, 245556042, 1744312007, 1352636452])
        
    def testGenseq02(self):
        self.assertEqual(genseq(8921, 48271, 5), [430625591, 1233683848, 1431495498, 137874439, 285222916])
     
    def testJudge01(self):
        self.assertTrue(judge(245556042, 1431495498))
        
    def testJudge02(self):
        self.assertFalse(judge(1092455, 430625591))
        
if __name__ == '__main__':
    unittest.main()