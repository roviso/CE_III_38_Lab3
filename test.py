import unittest
from bst import BinarySearchTree

class BSTTestCase(unittest.TestCase):
	
	def test_bstTest(self):
		bst = BinarySearchTree()
		
		bst.insert(10, 30)
		self.assertEqual(bst.size(),1)
		
		bst.insert(5, 320)
		self.assertEqual(bst.size(),2)
		
		bst.insert(30, 301)
		self.assertEqual(bst.size(),3)
		
		
		self.assertListEqual(bst.inorder_walk(),[5,10,30])
		self.assertListEqual(bst.preOrderWalk(), [10, 5, 30])
		self.assertListEqual(bst.postOrderWalk(), [5, 30, 10])
		
		bst.insert(15, 20)
		self.assertListEqual(bst.inorder_walk(),[5,10,15,30])
		

if __name__ == "__main__":
	unittest.main()
