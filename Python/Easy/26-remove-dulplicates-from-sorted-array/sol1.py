from typing import List
"""
Solution 1 for Leetcode 26 - Remove Duplicates from Sorted Array

Approach:
- Use two pointers:
    - `i` to iterate through the array.
    - `j` to mark the position of the next unique element.
- Since the array is sorted, duplicates will be adjacent.
- Start both pointers at index 1.
- Compare the current element (`nums[i]`) with the last unique element (`nums[j-1]`):
    - If they are different, assign `nums[j] = nums[i]` and increment `j`.
    - If they are the same, continue to the next `i`.
- After the loop, the first `j` elements in the array will be unique.

Time Complexity: O(n) - 'n' is the length of the array
Space Complexity: O(1) - No extra space used
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[j-1]:
                nums[j] = nums[i]
                j += 1
        return j 