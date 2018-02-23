import unittest
from solution17 import short_circuit, spinlock

class Solution17Test(unittest.TestCase):
    def testExample(self):
        self.assertEqual(short_circuit(3, 4), 3)
        
    def testPuzzle(self):
        self.assertEqual(short_circuit(324), 1306)
        
    def testPuzzle(self):
        self.assertEqual(short_circuit(324, 1000000), 1306)
        
if __name__ == '__main__':
    # unittest.main()
    for x in range(90):
        buffer = spinlock(324, x+5)
        print(*(buffer))

        6,30,19