# Ryan Cheung, Dillain Desai, Francisco Ortega
# CS034 Advanced Python
# 04/27/25

# --- Part 1: Binary Tree Construction and Traversal ---
# (Code for Part 1 would go here - handled by your colleague)

# --- Part 2: Binary Search Tree (BST) Operations ---

class Node:
    """
    Represents a single node in the tree.
    Each node holds a value and pointers to its left and right children.
    """
    def __init__(self, value):
        self.value = value  # The data stored in this node (e.g., a number)
        self.left = None    # Pointer to the left child node (initially none)
        self.right = None   # Pointer to the right child node (initially none)

class BinarySearchTree:
    """
    Represents the entire Binary Search Tree.
    It manages the nodes and provides operations like insert, search, remove.
    """
    def __init__(self):
        """
        Initializes an empty Binary Search Tree.
        The 'root' is the starting point of the tree. If it's None, the tree is empty.
        """
        self.root = None # Start with no nodes

    # --- Insertion ---
    def insert(self, value):
        """
        Inserts a new node with the given value into the BST,
        maintaining the BST property:
        - All values in the left subtree are less than the node's value.
        - All values in the right subtree are greater than or equal to the node's value.
        """
        new_node = Node(value) # Create a new box (Node) for the value

        # Case 1: Tree is empty
        if self.root is None:
            self.root = new_node # The new node becomes the starting point (root)
            return # We're done inserting

        # Case 2: Tree is not empty
        current = self.root # Start searching from the root
        while True: # Keep searching until we find an empty spot
            # Go Left?
            if value < current.value:
                if current.left is None: # Is the left spot empty?
                    current.left = new_node # Place the new node here
                    return # We're done
                else:
                    current = current.left # Move to the left child and continue searching
            # Go Right?
            else: # value >= current.value
                if current.right is None: # Is the right spot empty?
                    current.right = new_node # Place the new node here
                    return # We're done
                else:
                    current = current.right # Move to the right child and continue searching

    # --- Searching ---
    def search(self, value):
        """
        Searches for a node with the given value in the BST.
        Returns True if the value is found, False otherwise.
        It leverages the BST property for efficiency.
        """
        current = self.root # Start at the root
        while current is not None: # Keep searching as long as we are on a valid node
            if value == current.value:
                return True # Found it!
            elif value < current.value:
                current = current.left # Value might be in the left subtree
            else: # value > current.value
                current = current.right # Value might be in the right subtree
        # If the loop finishes (current becomes None), we didn't find it
        return False

    # --- Traversal ---
    def inorder(self):
        """
        Performs an inorder traversal (Left -> Node -> Right) of the BST.
        For a BST, this will always print the values in sorted order.
        Uses a helper function to handle the recursion.
        """
        print("Inorder:", end=" ") # Label the output
        def _inorder(node):
            # Base case: If the node is None (empty spot), do nothing
            if node is not None:
                # 1. Go Left (Recursively)
                _inorder(node.left)
                # 2. Visit Node (Print its value)
                print(node.value, end=" ")
                # 3. Go Right (Recursively)
                _inorder(node.right)

        _inorder(self.root) # Start the traversal from the root
        print()  # Print a newline at the end for clean output

    # --- Removal Helper ---
    def min_value_node(self, node):
        """
        Helper function to find the node with the minimum value
        in the subtree starting at 'node'. In a BST, this is
        always the leftmost node in that subtree.
        Used by the remove function when deleting a node with two children.
        """
        current = node
        # Keep going left until we can't anymore
        while current.left is not None:
            current = current.left
        return current # This is the node with the minimum value

    # --- Removal ---
    def remove(self, value):
        """
        Removes a node with the given value from the BST.
        Handles three cases:
        1. Node to remove has no children.
        2. Node to remove has one child.
        3. Node to remove has two children.
        Uses a recursive helper function `_remove`.
        """
        def _remove(node, value):
            # Base Case: If we reach an empty spot (None), the value wasn't found
            if node is None:
                return node # Return None (or the empty spot)

            # Step 1: Find the node to remove
            if value < node.value:
                # Go left. The result of removing from the left subtree
                # becomes the new left child of the current node.
                node.left = _remove(node.left, value)
            elif value > node.value:
                # Go right. The result of removing from the right subtree
                # becomes the new right child.
                node.right = _remove(node.right, value)
            else:
                # Step 2: Node found! Now handle the removal cases.
                # Case 1 & 2: Node has 0 or 1 child
                if node.left is None:
                    # If no left child, replace node with its right child (or None)
                    return node.right
                elif node.right is None:
                    # If no right child, replace node with its left child
                    return node.left

                # Case 3: Node has two children
                # Find the inorder successor (smallest value in the right subtree)
                temp = self.min_value_node(node.right)

                # Copy the inorder successor's value to this node
                node.value = temp.value

                # Delete the inorder successor from the right subtree
                # (This successor will have 0 or 1 child, handled by previous cases)
                node.right = _remove(node.right, temp.value)

            # Return the node (potentially updated) to reconnect the tree
            return node

        # Start the recursive removal process from the root
        # The result of the removal becomes the new root of the tree
        self.root = _remove(self.root, value)

# --- Main Execution Block ---
if __name__ == '__main__':
    ''' runs only when the script is executed directly, not when it's imported as a module.'''
    print("Part 2: Binary Search Tree (BST) Operations")
    print("-------------------------------------------")
    
    # Create an empty BST
    bst = BinarySearchTree()
    
    # Insert the values as specified in the prompt
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]
    print(f"Inserting values: {values_to_insert}")
    for value in values_to_insert:
        bst.insert(value)
    
    # Print inorder traversal to verify sorted order
    print(f"Inorder traversal after insertion: {bst.inorder()}")
    # Expected output: 20 30 40 50 60 70 80
    
    # Search for values as specified in the prompt
    search_values = [40, 100, 60]
    print("\nSearching for values:")
    for value in search_values:
        result = bst.search(value)
        print(f"Value {value}: {'Found' if result else 'Not found'}")
    # Expected: 40 (Found), 100 (Not found), 60 (Found)
    
    # Remove nodes as specified in the prompt
    
    # Remove node with no children (20)
    print("\nRemoving node with no children (20):")
    bst.remove(20)
    print(f"Inorder traversal after removing 20: {bst.inorder()}")
    # Expected: 30 40 50 60 70 80
    
    # Remove node with one child (30)
    print("\nRemoving node with one child (30):")
    bst.remove(30)
    print(f"Inorder traversal after removing 30: {bst.inorder()}")
    # Expected: 40 50 60 70 80
    
    # Remove node with two children (50)
    print("\nRemoving node with two children (50):")
    bst.remove(50)
    print(f"Inorder traversal after removing 50: {bst.inorder()}")
    # Expected: 40 60 70 80
