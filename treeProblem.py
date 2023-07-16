"""
For this problem, you will learn how to traverse the BST.

I have created the tree and written the insert function for the tree.
"""
# Create a class called BST where we will create a BST
class BST:
    """
    Creating a class called node to handle our inital data
    """
    class Node:
        """
        Establiches that our nodes have data. 
        Each node is linked. 
        Doesn't matter what side it is on. 
        """
        def __init__(self, data):
            """ 
            Initialize the data (number), left, and right side to be empty.
            """
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize the root to be empty. 
        """
        self.root = None

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left subtree.
                self._insert(data, node.left)
        elif data >= node.data:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right subtree.
                self._insert(data, node.right)

    def __iter__(self):
        """
        This is will help the traversal work. 
        It is initilazed when a loop is preformed. 
        """
        yield from self._traverse(self.root)  # Start at the root
        
    def _traverse(self, node):
        """
        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        TIP: I have left the structure for you.
        Fill in the ???s.
        """
        if node is not "???":
            yield from "???"
            yield node.data
            yield from "???"

# Inserting into the tree so that you have data to traverse through.
tree = BST()
tree.insert(8)
tree.insert(10)
tree.insert(6)
tree.insert(4)
tree.insert(13)
tree.insert(11)
tree.insert(5)

# Will show if your program is traversing. 
for x in tree:
    print(x)
