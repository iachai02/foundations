# DSA Curriculum — Neetcode 150

Problems in order. Do not skip. Check off as completed. Source: https://neetcode.io/roadmap

Legend: ✅ done | 🔁 in SRS queue | ⬜ not started

---

## Arrays & Hashing

| # | Problem | Difficulty | LC # | Status |
|---|---------|------------|------|--------|
| 1 | Contains Duplicate | Easy | 217 | ⬜ |
| 2 | Valid Anagram | Easy | 242 | ⬜ |
| 3 | Two Sum | Easy | 1 | ⬜ |
| 4 | Group Anagrams | Medium | 49 | ⬜ |
| 5 | Top K Frequent Elements | Medium | 347 | ⬜ |
| 6 | Product of Array Except Self | Medium | 238 | ⬜ |
| 7 | Valid Sudoku | Medium | 36 | ⬜ |
| 8 | Encode and Decode Strings | Medium | NeetCode | ⬜ |
| 9 | Longest Consecutive Sequence | Medium | 128 | ⬜ |

**Pattern to understand**: Hash maps for O(1) lookup. Anagram detection via frequency maps. Bucket sort for top-K.

---

## Two Pointers

| # | Problem | Difficulty | LC # | Status |
|---|---------|------------|------|--------|
| 10 | Valid Palindrome | Easy | 125 | ⬜ |
| 11 | Two Sum II - Input Array Is Sorted | Medium | 167 | ⬜ |
| 12 | 3Sum | Medium | 15 | ⬜ |
| 13 | Container With Most Water | Medium | 11 | ⬜ |
| 14 | Trapping Rain Water | Hard | 42 | ⬜ |

**Pattern to understand**: Two pointers work on sorted arrays or when you can shrink a window from both ends. Know when to move left vs right.

---

## Sliding Window

| # | Problem | Difficulty | LC # | Status |
|---|---------|------------|------|--------|
| 15 | Best Time to Buy and Sell Stock | Easy | 121 | ⬜ |
| 16 | Longest Substring Without Repeating Characters | Medium | 3 | ⬜ |
| 17 | Longest Repeating Character Replacement | Medium | 424 | ⬜ |
| 18 | Permutation in String | Medium | 567 | ⬜ |
| 19 | Minimum Window Substring | Hard | 76 | ⬜ |
| 20 | Sliding Window Maximum | Hard | 239 | ⬜ |

**Pattern to understand**: Expand right, shrink left when constraint is violated. Use a frequency map or deque inside the window.

---

## Stack

| # | Problem | Difficulty | LC # | Status |
|---|---------|------------|------|--------|
| 21 | Valid Parentheses | Easy | 20 | ⬜ |
| 22 | Min Stack | Medium | 155 | ⬜ |
| 23 | Evaluate Reverse Polish Notation | Medium | 150 | ⬜ |
| 24 | Generate Parentheses | Medium | 22 | ⬜ |
| 25 | Daily Temperatures | Medium | 739 | ⬜ |
| 26 | Car Fleet | Medium | 853 | ⬜ |
| 27 | Largest Rectangle in Histogram | Hard | 84 | ⬜ |

**Pattern to understand**: Monotonic stack for "next greater/smaller element" problems. Stack for matching/pairing.

---

## Binary Search

| # | Problem | Difficulty | LC # | Status |
|---|---------|------------|------|--------|
| 28 | Binary Search | Easy | 704 | ⬜ |
| 29 | Search a 2D Matrix | Medium | 74 | ⬜ |
| 30 | Koko Eating Bananas | Medium | 875 | ⬜ |
| 31 | Find Minimum in Rotated Sorted Array | Medium | 153 | ⬜ |
| 32 | Search in Rotated Sorted Array | Medium | 33 | ⬜ |
| 33 | Time Based Key-Value Store | Medium | 981 | ⬜ |
| 34 | Median of Two Sorted Arrays | Hard | 4 | ⬜ |

**Pattern to understand**: Binary search on the answer (not just on an array). Recognize when to binary search on a value range, not an index.

---

## Linked List

| # | Problem | Difficulty | LC # | Status |
|---|---------|------------|------|--------|
| 35 | Reverse Linked List | Easy | 206 | ⬜ |
| 36 | Merge Two Sorted Lists | Easy | 21 | ⬜ |
| 37 | Reorder List | Medium | 143 | ⬜ |
| 38 | Remove Nth Node From End of List | Medium | 19 | ⬜ |
| 39 | Copy List with Random Pointer | Medium | 138 | ⬜ |
| 40 | Add Two Numbers | Medium | 2 | ⬜ |
| 41 | Linked List Cycle | Easy | 141 | ⬜ |
| 42 | Find the Duplicate Number | Medium | 287 | ⬜ |
| 43 | LRU Cache | Medium | 146 | ⬜ |
| 44 | Merge K Sorted Lists | Hard | 23 | ⬜ |
| 45 | Reverse Nodes in K-Group | Hard | 25 | ⬜ |

**Pattern to understand**: Fast/slow pointers (Floyd's cycle). Dummy head node. Drawing pointer rewiring before coding.

---

## Trees

| # | Problem | Difficulty | LC # | Status |
|---|---------|------------|------|--------|
| 46 | Invert Binary Tree | Easy | 226 | ⬜ |
| 47 | Maximum Depth of Binary Tree | Easy | 104 | ⬜ |
| 48 | Diameter of Binary Tree | Easy | 543 | ⬜ |
| 49 | Balanced Binary Tree | Easy | 110 | ⬜ |
| 50 | Same Tree | Easy | 100 | ⬜ |
| 51 | Subtree of Another Tree | Easy | 572 | ⬜ |
| 52 | Lowest Common Ancestor of a BST | Medium | 235 | ⬜ |
| 53 | Binary Tree Level Order Traversal | Medium | 102 | ⬜ |
| 54 | Binary Tree Right Side View | Medium | 199 | ⬜ |
| 55 | Count Good Nodes in Binary Tree | Medium | 1448 | ⬜ |
| 56 | Validate Binary Search Tree | Medium | 98 | ⬜ |
| 57 | Kth Smallest Element in a BST | Medium | 230 | ⬜ |
| 58 | Construct Binary Tree from Preorder and Inorder | Medium | 105 | ⬜ |
| 59 | Binary Tree Maximum Path Sum | Hard | 124 | ⬜ |
| 60 | Serialize and Deserialize Binary Tree | Hard | 297 | ⬜ |

**Pattern to understand**: DFS (recursive) vs BFS (iterative with queue). In-order traversal of BST gives sorted order. Return values from recursive calls.

---

## Tries

| # | Problem | Difficulty | LC # | Status |
|---|---------|------------|------|--------|
| 61 | Implement Trie (Prefix Tree) | Medium | 208 | ⬜ |
| 62 | Design Add and Search Words | Medium | 211 | ⬜ |
| 63 | Word Search II | Hard | 212 | ⬜ |

**Pattern to understand**: Trie = tree of characters. Each node has children dict + is_end flag. Walk character by character.

---

## Heap / Priority Queue

| # | Problem | Difficulty | LC # | Status |
|---|---------|------------|------|--------|
| 64 | Kth Largest Element in a Stream | Easy | 703 | ⬜ |
| 65 | Last Stone Weight | Easy | 1046 | ⬜ |
| 66 | K Closest Points to Origin | Medium | 973 | ⬜ |
| 67 | Kth Largest Element in an Array | Medium | 215 | ⬜ |
| 68 | Task Scheduler | Medium | 621 | ⬜ |
| 69 | Design Twitter | Medium | 355 | ⬜ |
| 70 | Find Median from Data Stream | Hard | 295 | ⬜ |

**Pattern to understand**: Min-heap for "top K largest". Max-heap for "top K smallest". Two-heap trick for dynamic median.

---

## Backtracking

| # | Problem | Difficulty | LC # | Status |
|---|---------|------------|------|--------|
| 71 | Subsets | Medium | 78 | ⬜ |
| 72 | Combination Sum | Medium | 39 | ⬜ |
| 73 | Combination Sum II | Medium | 40 | ⬜ |
| 74 | Permutations | Medium | 46 | ⬜ |
| 75 | Subsets II | Medium | 90 | ⬜ |
| 76 | Word Search | Medium | 79 | ⬜ |
| 77 | Palindrome Partitioning | Medium | 131 | ⬜ |
| 78 | Letter Combinations of a Phone Number | Medium | 17 | ⬜ |
| 79 | N-Queens | Hard | 51 | ⬜ |

**Pattern to understand**: Choose / explore / unchoose. Decision tree. Pruning with constraints. `used[]` vs index-based deduplication.

---

## Graphs

| # | Problem | Difficulty | LC # | Status |
|---|---------|------------|------|--------|
| 80 | Number of Islands | Medium | 200 | ⬜ |
| 81 | Clone Graph | Medium | 133 | ⬜ |
| 82 | Max Area of Island | Medium | 695 | ⬜ |
| 83 | Pacific Atlantic Water Flow | Medium | 417 | ⬜ |
| 84 | Surrounded Regions | Medium | 130 | ⬜ |
| 85 | Rotting Oranges | Medium | 994 | ⬜ |
| 86 | Walls and Gates | Medium | 286 | ⬜ |
| 87 | Course Schedule | Medium | 207 | ⬜ |
| 88 | Course Schedule II | Medium | 210 | ⬜ |
| 89 | Redundant Connection | Medium | 684 | ⬜ |
| 90 | Number of Connected Components | Medium | 323 | ⬜ |
| 91 | Graph Valid Tree | Medium | 261 | ⬜ |
| 92 | Word Ladder | Hard | 127 | ⬜ |

**Pattern to understand**: DFS for connectivity/flood fill. BFS for shortest path. Topological sort for dependency ordering. Union-Find for connected components.

---

## Advanced Graphs

| # | Problem | Difficulty | LC # | Status |
|---|---------|------------|------|--------|
| 93 | Reconstruct Itinerary | Hard | 332 | ⬜ |
| 94 | Min Cost to Connect All Points | Medium | 1584 | ⬜ |
| 95 | Network Delay Time | Medium | 743 | ⬜ |
| 96 | Swim in Rising Water | Hard | 778 | ⬜ |
| 97 | Alien Dictionary | Hard | 269 | ⬜ |
| 98 | Cheapest Flights Within K Stops | Medium | 787 | ⬜ |

**Pattern to understand**: Dijkstra (min-heap + visited). Prim's/Kruskal's for MST. Euler path conditions.

---

## 1-D Dynamic Programming

| # | Problem | Difficulty | LC # | Status |
|---|---------|------------|------|--------|
| 99 | Climbing Stairs | Easy | 70 | ⬜ |
| 100 | Min Cost Climbing Stairs | Easy | 746 | ⬜ |
| 101 | House Robber | Medium | 198 | ⬜ |
| 102 | House Robber II | Medium | 213 | ⬜ |
| 103 | Longest Palindromic Substring | Medium | 5 | ⬜ |
| 104 | Palindromic Substrings | Medium | 647 | ⬜ |
| 105 | Decode Ways | Medium | 91 | ⬜ |
| 106 | Coin Change | Medium | 322 | ⬜ |
| 107 | Maximum Product Subarray | Medium | 152 | ⬜ |
| 108 | Word Break | Medium | 139 | ⬜ |
| 109 | Longest Increasing Subsequence | Medium | 300 | ⬜ |
| 110 | Partition Equal Subset Sum | Medium | 416 | ⬜ |

**Pattern to understand**: Define dp[i] clearly. Find the recurrence. Build bottom-up. Recognize subproblems.

---

## 2-D Dynamic Programming

| # | Problem | Difficulty | LC # | Status |
|---|---------|------------|------|--------|
| 111 | Unique Paths | Medium | 62 | ⬜ |
| 112 | Longest Common Subsequence | Medium | 1143 | ⬜ |
| 113 | Best Time to Buy and Sell Stock with Cooldown | Medium | 309 | ⬜ |
| 114 | Coin Change II | Medium | 518 | ⬜ |
| 115 | Target Sum | Medium | 494 | ⬜ |
| 116 | Interleaving String | Medium | 97 | ⬜ |
| 117 | Longest Increasing Path in a Matrix | Hard | 329 | ⬜ |
| 118 | Distinct Subsequences | Hard | 115 | ⬜ |
| 119 | Edit Distance | Medium | 72 | ⬜ |
| 120 | Burst Balloons | Hard | 312 | ⬜ |
| 121 | Regular Expression Matching | Hard | 10 | ⬜ |

---

## Greedy

| # | Problem | Difficulty | LC # | Status |
|---|---------|------------|------|--------|
| 122 | Maximum Subarray | Medium | 53 | ⬜ |
| 123 | Jump Game | Medium | 55 | ⬜ |
| 124 | Jump Game II | Medium | 45 | ⬜ |
| 125 | Gas Station | Medium | 134 | ⬜ |
| 126 | Hand of Straights | Medium | 846 | ⬜ |
| 127 | Merge Triplets to Form Target Triplet | Medium | 1899 | ⬜ |
| 128 | Partition Labels | Medium | 763 | ⬜ |
| 129 | Valid Parenthesis String | Medium | 678 | ⬜ |

---

## Intervals

| # | Problem | Difficulty | LC # | Status |
|---|---------|------------|------|--------|
| 130 | Insert Interval | Medium | 57 | ⬜ |
| 131 | Merge Intervals | Medium | 56 | ⬜ |
| 132 | Non-Overlapping Intervals | Medium | 435 | ⬜ |
| 133 | Meeting Rooms | Easy | 252 | ⬜ |
| 134 | Meeting Rooms II | Medium | 253 | ⬜ |
| 135 | Minimum Interval to Include Each Query | Hard | 1851 | ⬜ |

---

## Math & Geometry

| # | Problem | Difficulty | LC # | Status |
|---|---------|------------|------|--------|
| 136 | Rotate Image | Medium | 48 | ⬜ |
| 137 | Spiral Matrix | Medium | 54 | ⬜ |
| 138 | Set Matrix Zeroes | Medium | 73 | ⬜ |
| 139 | Happy Number | Easy | 202 | ⬜ |
| 140 | Plus One | Easy | 66 | ⬜ |
| 141 | Pow(x, n) | Medium | 50 | ⬜ |
| 142 | Multiply Strings | Medium | 43 | ⬜ |
| 143 | Detect Squares | Medium | 2013 | ⬜ |

---

## Bit Manipulation

| # | Problem | Difficulty | LC # | Status |
|---|---------|------------|------|--------|
| 144 | Single Number | Easy | 136 | ⬜ |
| 145 | Number of 1 Bits | Easy | 191 | ⬜ |
| 146 | Counting Bits | Easy | 338 | ⬜ |
| 147 | Reverse Bits | Easy | 190 | ⬜ |
| 148 | Missing Number | Easy | 268 | ⬜ |
| 149 | Sum of Two Integers | Medium | 371 | ⬜ |
| 150 | Reverse Integer | Medium | 7 | ⬜ |
