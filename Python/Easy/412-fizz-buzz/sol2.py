from typing import List
"""
Solution 2 for Leetcode 412 - Fizz Buzz

Approach:
- Use for loop and make a list to add 'Fizz' for multiples of 3,
 'Buzz' for multiples of 5 and 'FizzBuzz' for multiples of both 3 and 5 as list items 

Time Complexity: O(n) - where 'n' is the range of input
Space Complexity: O(n) - where 'n' is the number of output list items
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lst = []
        for i in range(1, n+1):
            if i%15 == 0:
                lst.append('FizzBuzz')
            elif i%5 == 0:
                lst.append('Buzz')
            elif i%3 == 0:
                lst.append('Fizz')
            else:
                lst.append(str(i))
        return lst
    
if __name__ == "__main__": # test_case run
    sol = Solution()
    n = 20
    print(sol.fizzBuzz(n)) 