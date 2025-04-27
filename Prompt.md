
🔬 CS 034 – Lab: Working with Trees (Chapter 9)
🎯 Objectives

By the end of this lab, students will be able to:

    Implement and traverse binary trees.

    Construct and manipulate binary search trees (BSTs).

    Apply recursive algorithms for traversal, insertion, and deletion.

    Explore self-balancing AVL tree insertions (challenge portion).

📁 Part 1: Binary Tree Construction and Traversal (15 pts)

Task:
Write a Python program that defines a binary tree using a Node class and constructs the following tree:
mathematica
CopyEdit
A / \ B C / \ \ D E F

    Create the tree structure in code using Node objects.

    Implement the following recursive traversals:

        Preorder

        Inorder

        Postorder

    Print the result of each traversal on the sample tree.

Requirements:

    Use recursion for traversals.

    Clearly label the output of each traversal.

📁 Part 2: Binary Search Tree (BST) Operations (15 pts)

Task:
Implement a Binary Search Tree (BST) with the following operations:

    insert(value)

    search(value)

    remove(value)

    inorder() traversal to verify structure

Steps:

    Start with an empty BST.

    Insert the following values in order: 50, 30, 70, 20, 40, 60, 80

    Print the tree contents in inorder to verify sorted order.

    Search for values 40, 100, and 60 – indicate whether each was found.

    Remove nodes: one with no child (20), one with one child (30), and one with two children (50). Print the inorder traversal after each removal.

🌟 Challenge Part (Extra Credit: 5 pts)

Implement AVL Tree insertion for the same list: 50, 30, 70, 20, 40, 60, 80
Ensure the tree self-balances by applying rotations. You may include balance-factor computation and visual output using indentation or any tree visualization library.
📌 Submission Checklist

    ✅ Python file with all class and function definitions.

    ✅ Output printed clearly and labeled.

    ✅ Comments explaining each major function and traversal.

    ✅ Your name, course section, and date at the top of your file.

 
📊 Lab Rubric – Chapter 9: Trees (Total: 30 points + 5 extra credit)
Criteria 	Points 	Notes
Part 1: Binary Tree Construction & Traversals 	15 pts 	
- Tree structure built correctly 	3 pts 	Correct Node class and tree setup
- Preorder traversal implemented and correct 	3 pts 	Output matches expected order
- Inorder traversal implemented and correct 	3 pts 	Output matches expected order
- Postorder traversal implemented and correct 	3 pts 	Output matches expected order
- Clean, readable output and code structure 	3 pts 	Includes comments and labels
		
Part 2: Binary Search Tree (BST) Implementation 	15 pts 	
- Insert function works and builds valid BST 	3 pts 	BST properties respected
- Inorder traversal confirms correct structure 	2 pts 	Sorted output shown
- Search function works as expected 	3 pts 	Correct found/not found messages
- Remove function handles all 3 cases 	4 pts 	No child, one child, two children
- Output is clearly labeled after each operation 	3 pts 	Each step documented
		
Extra Credit: AVL Tree Insertion (Challenge) 	+5 pts 	
- Correct balance factor tracking 	2 pts 	Must trigger balancing logic
- Proper rotations applied (LL, RR, LR, RL) 	2 pts 	Manual or automated
- Inorder output of balanced tree shown 	1 pt 	Must match sorted input
🔖 Deductions (as needed)

    ❌ -2 pts: Missing student name or course info

    ❌ -2 to -5 pts: Missing or incorrect traversal output

    ❌ -5 pts: Logic errors in insert/remove that break BST rules

    ❌ -3 pts: Code lacks comments or is difficult to follow

