import unittest
from solution17 import short_circuit, after_zero, spinlock

class Solution17Test(unittest.TestCase):
    def testExample01(self):
        self.assertEqual(short_circuit(3, 4), 3)
        
    def testPuzzle01(self):
        self.assertEqual(short_circuit(324), 1306)
        
    def testPuzzle02(self):
        self.assertEqual(after_zero(324), -1)
        
if __name__ == '__main__':
    unittest.main()
    # for x in range(90):
        # buffer = spinlock(324, x+5)
        # print(*(buffer))
