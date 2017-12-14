import unittest
import solution03

class Solution03Test(unittest.TestCase):
    def testExample01(self):
        self.assertEqual(solution03.calc_steps(1), 0)
   
    def testExample02(self):
        self.assertEqual(solution03.calc_steps(12), 3)
       
    def testExample03(self):
        self.assertEqual(solution03.calc_steps(23), 2)
     
    def testExample01(self):
        self.assertEqual(solution03.calc_steps(1024), 31)
       
    def testPuzzle(self):
        self.assertEqual(solution03.calc_steps(368078), 371)

if __name__ == '__main__':
    unittest.main()
