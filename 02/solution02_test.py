import unittest
import solution02

class Solution02Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.example = 'example_input.txt'
        self.example2 = 'example_input2.txt'
        self.puzzle = 'puzzle_input.txt'
    
    def testExample(self):
        self.assertEqual(solution02.checksum(self.example), 18)

    def testPuzzle(self):
        self.assertEqual(solution02.checksum(self.puzzle), 50376)

    def testExample2(self):
        self.assertEqual(solution02.checksum2(self.example2), 9)

    def testPuzzle2(self):
        self.assertEqual(solution02.checksum2(self.puzzle), 267)
        
if __name__ == '__main__':
    unittest.main()