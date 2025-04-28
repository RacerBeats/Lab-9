# Francisco Ortega (responsible for the insert and search methods), ID: 10758041
# Ryan Cheung (responsible for the inorder, remove, and min value methods, and the testing), ID: 10754470
# Group Members: Dillan Desai, Ryan Cheung, Francisco Ortega
# Course Section: CS 034 - 39575
# Prof. Ashraf
# 4/27/25
# Chapter 9 Lab: Working with Trees

# This code implements a Binary Search Tree (BST) with methods for insertion, searching, and removal of nodes.
# It also includes an inorder traversal method to print the values in sorted order.

class Node:
    """
    Represents a node in a binary search tree (BST).
    Each node has a key (value) and pointers to its left and right children.
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    """
    A class representing a Binary Search Tree (BST).
    The BST supports insertion, searching, and removal of nodes.
    It also provides an inorder traversal method to print the values in sorted order.
    """
    def __init__(self):
        self.root = None

    # Inserting
    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            currentNode = self.root
            while True:
                # If the new node's key is less than the current node's key,
                if node.key < currentNode.key:
                    if currentNode.left is None:
                        currentNode.left = node
                        break # Inserted, exit the loop
                    else:
                        currentNode = currentNode.left
                else:
                    if currentNode.right is None:
                        currentNode.right = node
                        break # Inserted, exit the loop
                    else:
                        currentNode = currentNode.right

    # Searching - if found or not
    def search(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None
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
                print(node.key, end=" ")
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
    def remove(self, key):
        """
        Removes a node with the given value from the BST.
        Handles three cases:
        1. Node to remove has no children.
        2. Node to remove has one child.
        3. Node to remove has two children.
        Uses a recursive helper function `_remove`.
        """
        def _remove(node, key):
            # Base Case: If we reach an empty spot (None), the value wasn't found
            if node is None:
                return node # Return None (or the empty spot)

            # Step 1: Find the node to remove
            if key < node.key:
                # Go left. The result of removing from the left subtree
                # becomes the new left child of the current node.
                node.left = _remove(node.left, key)
            elif key > node.key:
                # Go right. The result of removing from the right subtree
                # becomes the new right child.
                node.right = _remove(node.right, key)
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
                node.key = temp.key

                # Delete the inorder successor from the right subtree
                # (This successor will have 0 or 1 child, handled by previous cases)
                node.right = _remove(node.right, temp.key)

            # Return the node (potentially updated) to reconnect the tree
            return node

        # Start the recursive removal process from the root
        # The result of the removal becomes the new root of the tree
        self.root = _remove(self.root, key)

print("Part 2: Binary Search Tree (BST) Operations")
print("-------------------------------------------")
    
# Create an empty BST
bst = BST()
    
# Insert the values as specified in the prompt
values_to_insert = [50, 30, 70, 20, 40, 60, 80]
print(f"Inserting values: {values_to_insert}")
for value in values_to_insert:
    bst.insert(Node(value))
    
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