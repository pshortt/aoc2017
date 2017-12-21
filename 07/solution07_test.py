import unittest
import solution07

class Solution07Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.example = solution07.Tower('example_input.txt')
        self.puzzle = solution07.Tower('puzzle_input.txt')
    
    def testExample(self):
        self.assertEqual(self.example.root.name, 'tknk')

    def testTotalWeight(self):
        self.assertEqual(self.example.get_program('padx').total_weight(), 243)
    def testPuzzle(self):
        self.assertEqual(self.puzzle.root.name, 'qibuqqg')

if __name__ == '__main__':
    unittest.main()
