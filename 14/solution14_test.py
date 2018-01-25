import unittest
from solution14 import generate_disk, count_blocks, neighbours, next_node, count_groups

class Solution14Test(unittest.TestCase):
    def testExample01(self):
        self.assertEqual(count_blocks('flqrgnkx'), 8108)

    def testPuzzle01(self):
        self.assertEqual(count_blocks('hfdlxzhv'), 8230)
        
    def testExample02(self):
        self.assertEqual(count_groups('flqrgnkx'), 1242)

    def testPuzzle02(self):
        self.assertEqual(count_groups('hfdlxzhv'), 1103)
    
    def testNeightbours01(self):
        self.assertEqual(neighbours((0,0)), [(1, 0), (0, 1)])
        
    def testNeightbours02(self):
        self.assertEqual(neighbours((69,127)), [(68, 127), (70, 127), (69, 126)])
        
    def testNeightbours03(self):
        self.assertEqual(neighbours((69,12)), [(68, 12), (70, 12), (69, 11), (69, 13)])
        
    # def testNeightbours04(self):
        # self.assertEqual(neighbours((69,127), [(70, 127), (69, 126)]), [(68, 127)])
    
    def testNextNode01(self):
        disk = [['0', '1', '1', '0'], 
                ['0', '1', '0', '0'], 
                ['0', '0', '0', '1'], 
                ['1', '1', '1', '1']]
        grouped_nodes = [(0,1), (0,2), (1,1)]
        self.assertEqual(next_node(disk, grouped_nodes), (2,3))
    
    def testNextNode02(self):
        disk = [['0', '1', '1', '0'], 
                ['0', '1', '0', '0'], 
                ['0', '0', '0', '1'], 
                ['1', '1', '1', '1']]
        grouped_nodes = []
        self.assertEqual(next_node(disk, grouped_nodes), (0,1))
        
    def testNextNode03(self):
        disk = [['0', '1', '1', '0'], 
                ['0', '1', '0', '0'], 
                ['0', '0', '0', '1'], 
                ['0', '0', '0', '0']]
        grouped_nodes = [(0,1), (0,2), (1,1), (2,3)]
        self.assertEqual(next_node(disk, grouped_nodes), None)
    
    
if __name__ == '__main__':
    unittest.main()
