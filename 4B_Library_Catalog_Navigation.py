# 4B Library Catalog Navigation

class Node:
    def __init__(self, book_id):
        self.book_id = book_id
        self.left = None
        self.right = None


# Insert a book into the Binary Search Tree
def insert(root, book_id):
    if root is None:
        return Node(book_id)

    if book_id < root.book_id:
        root.left = insert(root.left, book_id)
    elif book_id > root.book_id:
        root.right = insert(root.right, book_id)

    return root


# Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.book_id, end=" ")
        inorder(root.right)


# Preorder Traversal
def preorder(root):
    if root:
        print(root.book_id, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder Traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.book_id, end=" ")


# Main Program
root = None

user_input = input("Enter Book IDs separated by space: ")
books = user_input.split()

for book in books:
    root = insert(root, int(book))


print("\nInorder Traversal: ", end="")
inorder(root)

print("\nPreorder Traversal: ", end="")
preorder(root)

print("\nPostorder Traversal: ", end="")
postorder(root)