import unittest, os, time
from solution13 import Firewall
from solution13 import break_firewall

class Solution13Test(unittest.TestCase):
    def testExample01(self):
        f = Firewall('example_input.txt')
        self.assertEqual(f.severity, 24)

    def testPuzzle01(self):
        f = Firewall('puzzle_input.txt')
        self.assertEqual(f.severity, 1840)
    
    def testExample02(self):
        self.assertEqual(break_firewall('example_input.txt'), 10)

    def testPuzzle02(self):
        self.assertEqual(break_firewall('puzzle_input.txt'), 3850260)
        
if __name__ == '__main__':
    unittest.main()
    # start = time.time()
    # for i in range(10000):
        # break_firewall('example_input.txt')
    # end = time.time()
    # print(end - start)

