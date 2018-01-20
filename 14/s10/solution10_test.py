import unittest
from solution10 import KnotHash

class Solution10Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.example1 = KnotHash([3, 4, 1, 5], False, 5)
        self.example2 = KnotHash('\x03\x04\x01\x05', False, 5)
        self.example3 = KnotHash('', True)
        self.example4 = KnotHash('AoC 2017', True)
        self.example5 = KnotHash('1,2,3', True)
        self.example6 = KnotHash('1,2,4', True)
        
        self.puzzle1 = KnotHash([97,167,54,178,2,11,209,174,119,248,254,0,255,1,64,190], False)
        self.puzzle2 = KnotHash('a\xa76²\x02\x0bÑ\xaew\xf8\xfe\x00ÿ\x01@\xbe', False)
        self.puzzle3 = KnotHash('97,167,54,178,2,11,209,174,119,248,254,0,255,1,64,190', True)
        
    def testExample01(self):
        res = self.example1.sparse
        self.assertEqual(res[0]*res[1], 12)

    def testExample02(self):
        res = self.example2.sparse
        self.assertEqual(res[0]*res[1], 12)
        
    def testExample03(self):
        self.assertEqual(str(self.example3), 'a2582a3a0e66e6e86e3812dcb672a272')
    
    def testExample04(self):
        self.assertEqual(str(self.example4), '33efeb34ea91902bb2f59c9920caa6cd')
    
    def testExample05(self):
        self.assertEqual(str(self.example5), '3efbe78a8d82f29979031a4aa0b16a9d')
        
    def testExample05(self):
        self.assertEqual(str(self.example6), '63960835bcdc130f0b66d7ff4f6a5a8e')
        
    def testPuzzle01(self):
        res = self.puzzle1.sparse
        self.assertEqual(res[0]*res[1], 8536)
        
    def testPuzzle02(self):
        res = self.puzzle2.sparse
        self.assertEqual(res[0]*res[1], 8536)
        
    def testPuzzle03(self):
        self.assertEqual(str(self.puzzle3), '')       
    
if __name__ == '__main__':
    unittest.main()
