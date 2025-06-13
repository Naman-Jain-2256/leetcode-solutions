# Leetcode 26 - Remove Duplicates from Sorted Array

**🔗 Problem link**: [Leetcode 26 - Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

---

## 🧠 Problem Summary

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be preserved.

Return the number of unique elements in `nums`.  
You must do this in-place with `O(1)` extra memory.

> Consider the number of unique elements as `k`.  
> To get accepted, you need to:
- Modify `nums` such that the first `k` elements contain the unique elements.
- The remaining elements of `nums` beyond `k` are not important.

---

## ✅ Solution

### ✔️ Two-Pointer Approach

- **Approach**:
    - Use two pointers:
        - `i` to iterate through the array.
        - `j` to mark the position where the next unique element should be placed.
    - Since the array is sorted, duplicates will always be adjacent.
    - Start both pointers at index 1.
    - For each `nums[i]`:
        - If it's **not equal** to `nums[j - 1]`, assign `nums[j] = nums[i]` and increment `j`.
    - After the loop, the first `j` elements in `nums` are the unique ones.
    - Return `j`.

- **Time Complexity**: `O(n)` — where `n` is the length of the array.
- **Space Complexity**: `O(1)` — in-place, no extra space used.

---

## 🔎 Examples

```python
Input: nums = [1, 1, 2]
Output: 2, nums = [1, 2, _]
Explanation: Your function should return k = 2, 
with the first two elements of nums being 1 and 2 respectively. 
It doesn't matter what you leave beyond the returned k.

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5,
with the first five elements of nums being 0, 1, 2, 3, and 4 respectively. 
The rest can be ignored.
```