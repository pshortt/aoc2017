import sys, os

dirname = sys.argv[1]
os.mkdir(dirname)
os.chdir(dirname)
main_file = open('solution' + dirname + '.py', 'w+')
main_file.close()
test_file = open('solution' + dirname + '_test.py', 'w+')

test_file.write('import unittest\n')
test_file.write('from solution' + dirname + 'import\n')
test_file.write('\n')
test_file.write('class Solution'+ dirname + 'Test(unittest.TestCase):\n')
test_file.write('    def testExample(self):\n')
test_file.write('        self.assertTrue(True)\n')
test_file.write('\n')
test_file.write('    def testPuzzle(self):\n')
test_file.write('        self.assertTrue(True)\n')
test_file.write('\n')
test_file.write('if __name__ == \'__main__\':\n')
test_file.write('    unittest.main()\n')

main_file.close()
