# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment examined how Binary Search Trees (BSTs) organize data recursively, and how insertion order affects a tree's shape and search efficiency. I implemented a Pac-Man arcade high-score leaderboard, keyed by score, to demonstrate insertion, in-order traversal, and searching.

## What I Built

### Tree Construction; `insert()`, `_insert_recursive()`, and the leaderboard build (TODO 1-2)

`insert()` starts the recursion at the root and reassigns it to whatever `_insert_recursive()` returns. `_insert_recursive()` walks down the tree comparing the new value against the current node: smaller values recurse left, larger values recurse right, and the base case (`node is None`) creates the new node once an empty spot is found. Equal values fall through both comparisons and are silently skipped, since a leaderboard doesn't need the same score stored twice. I built the leaderboard by inserting `[5000, 3000, 8000, 1000, 4000, 7000, 9000]`; 5000 becomes the root, 3000 and 8000 land on either side of it, and 1000/4000 and 7000/9000 branch further into the left and right subtrees respectively, so the tree ends up populated on both sides.

### In-Order Traversal; `inorder()` and `_inorder_recursive()` (TODO 3)

`_inorder_recursive()` visits the left subtree, then the current node, then the right subtree. Because a BST already keeps every smaller value to the left of a node and every larger value to the right, this left-node-right visiting order reads the values back out in fully sorted order with no separate sorting step. Running it on the leaderboard returns `[1000, 3000, 4000, 5000, 7000, 8000, 9000]`.

### Search; `search()` and `_search_recursive()` (TODO 4)

`_search_recursive()` compares the target against the current node and recurses into only the one subtree that could possibly contain it, ruling out the other subtree entirely. That's what makes BST search faster than a linear scan of an unordered list: a linear search may have to check every element, while a balanced BST search only needs about `log2(n)` comparisons. I tested two scores on the leaderboard (8000, 1000) and two that were never inserted (6000, 2500), and each search returned the correct `True`/`False` result.

### Edge Cases (TODO 5)

Covers three cases: traversing and searching a completely empty leaderboard (returns `[]` and `False` without error), building a leaderboard with a single score and confirming both a present and a missing score search against it, and inserting the same score twice to confirm the duplicate is dropped rather than stored a second time.

### Real-World Scenario

A Pac-Man arcade high-score leaderboard **is** the real-world scenario: every new score is inserted into the tree, the leaderboard is displayed by traversing the tree in order, and checking whether a specific score is already on the board is a direct search operation.

## Balanced vs. Unbalanced BST Performance

A BST's efficiency depends entirely on how balanced it ends up, which is a direct result of insertion order. Inserting values that are already sorted (for example, scores added in strictly increasing order: 1000, 2000, 3000, 4000...) makes every new node attach only as a right child, degenerating the tree into what is effectively a linked list; search then becomes O(n) instead of O(log n), since every node has to be visited in sequence. Inserting the same values in a more balanced order (starting near the middle, then alternating higher and lower) keeps the tree's height close to `log2(n)`, so each comparison during search or insertion still eliminates about half of the remaining values. The leaderboard example in this assignment was inserted in an order that already branches both left and right (5000 root, with 3000/8000 splitting the next level), which is why every search in the SEARCH TESTS section only needed two or three comparisons instead of scanning the whole leaderboard.
