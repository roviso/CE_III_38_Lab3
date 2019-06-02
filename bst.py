class BinarySearchTree:
        def __init__(self):
                self._size = 0
                self._root = None

        class _BSTNode:
                def __init__(self,key,value):
                        self.left = None
                        self.right = None
                        self.key = key
                        self.value = value
                        self.parent = None
                
        def insert(self, key, value):
                y = None
                x = self._root
                z = self._BSTNode(key,value)
                while (x != None):
                        y = x
                        if (key < x.key):
                                x = x.left
                        else:
                                x = x.right
                z.parent = y
                if(y == None):
                        self._root = z
                elif (z.key < y.key):
                        y.left = z
                else:
                        y.right = z
                        
                self._size += 1



                        
        
        def search(self, x,k):
                if (x == None):
                        return False
                elif (x.key == k):
                        return True
                if k < x.key:
                        return self.search(x.left,k)
                else:
                        return self.search(x.right,k)
                        
        def smallest(self,x):
                while (x.left != None):
                        x = x.left
                return x.key
                
        def largest(self,x):
                while (x.right != None):
                        x = x.right
                return x.key
                
        def is_empty(self):
                return self._size == 0
                
        def size(self):
                return self._size

        def mintree(self,x):
                while(x.left != None):
                        x = x.left
                return x

        def searchnode(self,key):
                x=self._root
                y=None
                while(x!=None):
                    if(key==x.key):
                        return x
                    elif(key<x.key):
                        x=x.left
                    elif(key>x.key):
                        x=x.right
                return False

        def transplant(self,u,v):
                if (u.parent == None):
                        self._root = v
                elif (u == u.parent.left):
                        u.parent.left = v
                else:
                        u.parent.right = v
                if (v !=  None):
                        v.parent = u.parent

        def delete(self,x,key):
                z = self.searchnode(key)                
                if (z.left == None):
                        self.transplant(z,z.right)
                elif (z.right == None):
                        self.transplant(z,z.left)
                else:
                        y = self.mintree(z.right)
                        if (y.parent != z):
                                self.transplant(y,y.right)
                                y.right = z.right
                                y.right.parent = y
                        self.transplant(y,z)
                        y.left = z.left
                        y.left.parent = y
                        self._size -= 1

                        
                
        def inorder_walk(self):
                nodes = []
                self._inorder_walk(self._root,nodes)
                return nodes
                
        def _inorder_walk(self,subtree, nodes):
                if subtree:
                        self._inorder_walk(subtree.left, nodes)
                        nodes.append(subtree.key)
                        self._inorder_walk(subtree.right, nodes)



        def preOrderWalk(self):
                nodes = []
                self._preOrderWalk(self._root, nodes)
                return nodes

        def _preOrderWalk(self, subtree, nodes):
                if(subtree):
                    nodes.append(subtree.key)
                    self._preOrderWalk(subtree.left, nodes)
                    self._preOrderWalk(subtree.right, nodes)



        def postOrderWalk(self):
                nodes = []
                self._postOrderWalk(self._root, nodes)
                return nodes

        def _postOrderWalk(self, subtree, nodes):
                if(subtree):
                    self._preOrderWalk(subtree.left, nodes)
                    self._preOrderWalk(subtree.right, nodes)
                    nodes.append(subtree.key)


                                
        
        
x = BinarySearchTree()
x.insert(30,'r')
x.insert(20,'a')
x.insert(40,'w')
x.insert(9,'ar')
x.insert(35,'wa')
x.insert(50,'w')
x.insert(60,'wre')


print(x.inorder_walk())
print(x.search(x._root,9))

x.delete(x._root,50)

print(x.postOrderWalk())

print(x.search(x._root,9))

print(x.smallest(x._root))
print(x.largest(x._root))

print(x.preOrderWalk())

