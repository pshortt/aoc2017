import unittest
from solution14 import generate_disk, count_blocks, neighbours

class Solution14Test(unittest.TestCase):
    def testExample(self):
        self.assertEqual(count_blocks('flqrgnkx'), 8108)

    def testPuzzle(self):
        self.assertEqual(count_blocks('hfdlxzhv'), 8230)

if __name__ == '__main__':
    unittest.main()
    # print(neighbours((0,0), 128))
    # print(neighbours((127,0), 128))
    # print(neighbours((0,1), 128))
    # print(neighbours((69,127), 128))
    # print(neighbours((69,12), 128))