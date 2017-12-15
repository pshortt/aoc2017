import unittest
import solution03

class Solution03Test(unittest.TestCase):
    def testExample01(self):
        self.assertEqual(solution03.calc_steps(1, False), 0)
   
    def testExample02(self):
        self.assertEqual(solution03.calc_steps(12, False), 3)
       
    def testExample03(self):
        self.assertEqual(solution03.calc_steps(23, False), 2)
     
    def testExample01(self):
        self.assertEqual(solution03.calc_steps(1024, False), 31)
       
    def testPart1Puzzle(self):
        self.assertEqual(solution03.calc_steps(368078, False), 371)
    
    def testBuildSpiral(self):
        self.assertEqual(solution03.build_spiral(3, False),[(1, 0, 0),(2, 0, 1),(3, 1, 1),(4, 1, 0)])
    
    def testPart2Example01(self):
        self.assertEqual(solution03.calc_steps(4, True), 5)
    
    def testPart2Example02(self):
        self.assertEqual(solution03.calc_steps(5, True), 10)
    
    def testPart2Example03(self):
        self.assertEqual(solution03.calc_steps(3, True), 4)
        
    def testPart2Puzzle(self):
        self.assertEqual(solution03.calc_steps(369601, True), -1)
        
if __name__ == '__main__':
    unittest.main()
