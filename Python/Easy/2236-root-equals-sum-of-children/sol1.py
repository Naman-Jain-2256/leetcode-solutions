"""
Solution 1 for Leetcode 2236 - Root Equals Sum Of Children

Approach:
- Check if the root value is equal to the sum of its left and right child values.
- Assume that the tree has exactly 3 nodes as per problem constraints.

Time Complexity: O(1)
Space Complexity: O(1)
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.left.val+root.right.val==root.val
    

if __name__ == "__main__":
    # Example: root = 10, left = 4, right = 6 -> 4 + 6 == 10 -> True
    left_child = TreeNode(4)
    right_child = TreeNode(6)
    root = TreeNode(10,left_child,right_child)

    sol = Solution()
    print(sol.checkTree(root)) # output = True