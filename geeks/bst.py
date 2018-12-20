class BST:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.val),
        if self.right:
            self.right.PrintTree()

    def insert(self, val):
        if self.val >= val:
            if self.left:
                self.left = self.left.insert(val)
            else:
                self.left = BST(val)
        else:
            if self.right:
                self.right = self.right.insert(val)
            else:
                self.right = BST(val)
        return self
    
    def search(self, val):
        if self.val == val:
            return True
        elif self.val >= val:
            if self.left:
                return self.left.serach(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

root = BST(2)
root.insert(5)
root.insert(6)
root.insert(7)
root.insert(8)
root.PrintTree()
print
print root.search(8)
print root.search(4)



