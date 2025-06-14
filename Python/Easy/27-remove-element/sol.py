from typing import List

"""
✅ Solution for Leetcode 27 - Remove Element

🔹 Approach:
- Use two pointers:
    - `i` to track the position where the next non-`val` element should be placed.
    - Iterate through each element `num` in the list `nums`.
- If `num` is **not equal** to `val`, place it at index `i` and increment `i`.
- This effectively overwrites all instances of `val` while maintaining the order of other elements.

🔹 Time Complexity: O(n) - 'n' is the length of the array.
🔹 Space Complexity: O(1) - No extra space used.
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    k = sol.removeElement(nums, val)
    print(f'Output: {k}, modified nums: {nums[:k]}')

    print('\n')

    # Example 2
    nums2 = [3,2,2,3]
    val2 = 3
    k2 = sol.removeElement(nums2, val2)
    print(f'Output: {k2}, modified nums: {nums2[:k2]}')
