import unittest
from solution14 import generate_disk, count_blocks

class Solution14Test(unittest.TestCase):
    def testExample(self):
        self.assertEqual(count_blocks('flqrgnkx'), 8108)

    def testPuzzle(self):
        self.assertEqual(count_blocks('hfdlxzhv'), 8230)

if __name__ == '__main__':
    # unittest.main()
    # disk = generate_disk('flqrgnkx')
    # sum = 0
    # for row in disk:
        # print(row.replace('0', '.').replace('1', '#'))
    s = '11010100'
    ctr = 1
    r = ''
    for c in s:
        if c == '0':
            ctr += 1
            r += '.'
        else:
            r += str(ctr)
    print(r)