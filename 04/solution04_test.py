import unittest
import solution04

class Solution04Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.foo = 'bar'
        
    def testExample01(self):
        self.assertEqual(
            solution04.check_passphrase('aa bb cc dd ee', lambda x, y: x == y),
                                        True)
        
    def testExample02(self):
        self.assertEqual(
            solution04.check_passphrase('aa bb cc dd aa', lambda x, y: x == y),
                                        False)
        
    def testExample03(self):
        self.assertEqual(
            solution04.check_passphrase('aa bb cc dd aaa',lambda x, y: x == y),
                                        True) 
        
    def testPuzzle01(self):
        self.assertEqual(solution04.check_no_dupes('puzzle_input.txt'), 386)
    
    def testExample05(self):
        self.assertEqual(solution04.check_no_dupes('example_input1.txt'), 2)
        
    def testPuzzle02(self):
        self.assertEqual(solution04.check_no_anagrams('puzzle_input.txt'), 208)
    
    def testExample06(self):
        self.assertEqual(solution04.check_no_anagrams('example_input2.txt'), 3)
        
if __name__ == '__main__':
    unittest.main()
