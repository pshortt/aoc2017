import unittest
import solution08

class Solution08Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.example = solution08.InstructionSet('example_input.txt')
        self.puzzle = solution08.InstructionSet('puzzle_input.txt')
    
    def testExample01(self):
        self.assertEqual(self.example.largest_value(), 1)

    def testPuzzle01(self):
        self.assertEqual(self.puzzle.largest_value(), 3880)
        
    def testExample02(self):
        self.assertEqual(self.example.largest_hist_value(), 10)

    def testPuzzle02(self):
        self.assertEqual(self.puzzle.largest_hist_value(), 5035)   

        
if __name__ == '__main__':
    unittest.main()
