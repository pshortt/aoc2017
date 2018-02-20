import unittest
from solution15 import gen, count_matches

class Solution15Test(unittest.TestCase):
    def testExample01(self):
        self.assertEqual(count_matches(4*10**7, 65, 8921), 588)
        
    def testPuzzle01(self):
        self.assertEqual(count_matches(4*10**7, 516, 190), 597)
        
    def testExample02(self):
        self.assertEqual(count_matches(5*10**6, 65, 8921, 4, 8), 309)
        
    def testPuzzle02(self):
        self.assertEqual(count_matches(5*10**6, 516, 190, 4, 8), 303)

if __name__ == '__main__':
    unittest.main()

    
