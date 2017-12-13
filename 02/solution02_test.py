import unittest
import solution02

class Solution02Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.example = 'example_input.txt'
        self.puzzle = 'puzzle_input.txt'
    
    def testExample(self):
        self.assertEqual(solution02.checksum(self.example), 18)

    def testPuzzle(self):
        self.assertEqual(solution02.checksum(self.puzzle), 50376)
        
if __name__ == '__main__':
    unittest.main()