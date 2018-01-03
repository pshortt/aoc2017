import unittest
from solution09 import StreamProc

class Solution09Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        f = open('example_input.txt')
        self.examples = [StreamProc(l) for l in f]
        f.close()
        
        f = open('puzzle_input.txt')
        self.puzzle = StreamProc(f.readline())
        f.close()
        
    def testExample01(self):
        self.assertEqual(self.examples[0].totscore, 1)
    
    def testExample02(self):
        self.assertEqual(self.examples[1].totscore, 6)
        
    def testExample03(self):
        self.assertEqual(self.examples[2].totscore, 5)
    
    def testExample04(self):
        self.assertEqual(self.examples[3].totscore, 16)

    def testExample05(self):
        self.assertEqual(self.examples[4].totscore, 1)

    def testExample06(self):
        self.assertEqual(self.examples[5].totscore, 1)

    def testExample07(self):
        self.assertEqual(self.examples[6].totscore, 9)
        
    def testExample08(self):
        self.assertEqual(self.examples[7].totscore, 3)
        
    def testExample09(self):
        self.assertEqual(self.examples[8].totscore, 16)
        
    def testExample10(self):
        self.assertEqual(self.examples[9].totscore, 9)
    
    def testExample11(self):
        self.assertEqual(self.examples[10].ngarbage, 3)
    
    def testExample2_01(self):
        self.assertEqual(self.examples[0].ngarbage, 0)
    
    def testExample2_02(self):
        self.assertEqual(self.examples[1].ngarbage, 0)
        
    def testExample2_03(self):
        self.assertEqual(self.examples[2].ngarbage, 0)
    
    def testExample2_04(self):
        self.assertEqual(self.examples[3].ngarbage, 0)

    def testExample2_05(self):
        self.assertEqual(self.examples[4].ngarbage, 10)

    def testExample2_06(self):
        self.assertEqual(self.examples[5].ngarbage, 4)

    def testExample2_07(self):
        self.assertEqual(self.examples[6].ngarbage, 8)
        
    def testExample2_08(self):
        self.assertEqual(self.examples[7].ngarbage, 13)
        
    def testExample2_09(self):
        self.assertEqual(self.examples[8].ngarbage, 0)
        
    def testExample2_10(self):
        self.assertEqual(self.examples[9].ngarbage, 0)
    
    def testExample2_11(self):
        self.assertEqual(self.examples[10].ngarbage, 17)
    
    def testPuzzle(self):
        self.assertEqual(self.puzzle.totscore, 9251)
        
    def testPuzzle2(self):
        self.assertEqual(self.puzzle.ngarbage, 4322)

if __name__ == '__main__':
    unittest.main()
