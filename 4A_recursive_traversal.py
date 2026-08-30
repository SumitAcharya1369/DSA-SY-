# recursive traversal preorder-inorder-postorder

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def create():
    n=int(input("Enter data to create node :"))
    if n==0:
        return None
    root=Node(n) #object creation
    print(f"Enter left of {n}")
    root.left=create()
    print(f"Enter right of {n}")
    root.right=create()
    return root

def preorder(root):
    if root is not None:

        print(root.data)
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)


root=create()
postorder(root)


