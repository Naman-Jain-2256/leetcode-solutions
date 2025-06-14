# Leetcode 27 - Remove Element

**🔗 Problem link**: [Leetcode 27 -Remove Element](https://leetcode.com/problems/remove-element/)

---

## 🧠 Problem Summary 

- Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. 
    The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

- Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the 
    following things:

- Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`.
    The remaining elements of `nums` are not important as well as the size of `nums`.

- Return `k`.

---

## ✅ Solution

### ✔️ Two-Pointer Approach

- **Approach**:
    - Use two pointers:
        - `i` to track the position where a non-`val` element should be placed.
        - Iterate through each element `num` in the list `nums`.
    - If `num` **not equal** to `val`, place it at index `i` and increment `i`.
    - This effectively overwrites all instances of `val` while maintaining the order of other elements.

- **Time Complexity**: `O(n)` - where `n` is the length of the array.
- **Space Complexity**: `O(1)` - in-place, no extra space used.

---

### 🔎 Examples

```python

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
Note: The order of the returned elements does not matter.
It does not matter what you leave beyond the returned k (hence they are underscores).

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being any 5 numbers not equal to 2.
Note: The relative order does not matter.

```