from __future__ import print_function
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order(root):
    if root is None:
        return 
    
    queue = []
    queue.append(root)

    while(len(queue)>0):
        node = queue.pop(0)
        print(node.value, end=" ")
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

def preorder(root):
    if root is None:
        return
    print(root.value, end=" ")
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value, end=" ")

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.value, end=" ")
    inorder(root.right)



root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Preorder: ", end="")
preorder(root)
print()
print("Postorder: ", end="")
postorder(root)
print()
print("Inorder: ", end="")
inorder(root)
print()
print("Level-order: ", end="")
level_order(root)
print()



