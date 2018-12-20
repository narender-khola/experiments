class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        self.visited  =False
    
    def unvisited_child(self):
        if self.left and not self.left.visited:
            return self.left
        elif self.right and not self.right.visited:
            return self.right
        return None
    
    def preorder(self):
        stack = []
        self.visited = True
        print(self.data)
        stack.append(self)
        while len(stack) != 0:
            top = stack[len(stack)-1]
            unvisited_child = top.unvisited_child()
            if unvisited_child is not None:
                unvisited_child.visited = True
                print unvisited_child.data
                stack.append(unvisited_child)
            else:
                stack.pop()

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.preorder()