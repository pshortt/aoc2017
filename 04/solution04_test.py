import unittest
import solution04

class Solution04Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.foo = 'bar'
        
    def testExample01(self):
        self.assertEqual(solution04.check_passphrase('aa bb cc dd ee'), True)
        
    def testExample02(self):
        self.assertEqual(solution04.check_passphrase('aa bb cc dd aa'), False)
        
    def testExample03(self):
        self.assertEqual(solution04.check_passphrase('aa bb cc dd aaa'), True) 
        
    # def testExample04(self):
        # self.assertEqual(solution04.check_passphrase(''), '')
        
if __name__ == '__main__':
    unittest.main()
