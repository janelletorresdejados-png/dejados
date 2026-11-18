# Assessment 3.6: DFS Method in Tree
# Student: JANELLE

class Node:
    """Represents a single node in the binary tree."""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def dfs_preorder(root):
    """DFS Pre-order Traversal: Root -> Left -> Right"""
    if root:
        print(root.val, end=" ")
        dfs_preorder(root.left)
        dfs_preorder(root.right)

def dfs_inorder(root):
    """DFS In-order Traversal: Left -> Root -> Right"""
    if root:
        dfs_inorder(root.left)
        print(root.val, end=" ")
        dfs_inorder(root.right)

def dfs_postorder(root):
    """DFS Post-order Traversal: Left -> Right -> Root"""
    if root:
        dfs_postorder(root.left)
        dfs_postorder(root.right)
        print(root.val, end=" ")

if __name__ == "__main__":
    print("========================================")
    print("  Assessment 3.6: DFS Method in Tree")
    print("  Student: JANELLE")
    print("========================================\n")

    # Constructing a binary tree using the letters of "JANELLE":
    #          J
    #        /   \
    #       A     N
    #      / \   / \
    #     E   L L   E

    root = Node('J')
    root.left = Node('A')
    root.right = Node('N')
    root.left.left = Node('E')
    root.left.right = Node('L')
    root.right.left = Node('L')
    root.right.right = Node('E')

    print("Pre-order Traversal  : ", end="")
    dfs_preorder(root)
    print()

    print("In-order Traversal   : ", end="")
    dfs_inorder(root)
    print()

    print("Post-order Traversal : ", end="")
    dfs_postorder(root)
    print()
    print("\n----------------------------------------")