import unittest
from solution10 import tie_knot

class Solution10Test(unittest.TestCase):
    def testExample(self):
        self.assertEqual(tie_knot([3, 4, 1, 5], 5), 12)

    def testPuzzle(self):
        self.assertEqual(tie_knot([97,167,54,178,2,11,209,174,119,248,254,0,255,1,64,190]), 8536)

if __name__ == '__main__':
    unittest.main()
