from typing import List
"""
Solution 1 for Leetcode 412 - Fizz Buzz

Approach:
- Use List Comprehension to generate 'Fizz' for multiples of 3,
 'Buzz' for multiples of 5 and 'FizzBuzz' for multiples of both 3 and 5

Time Complexity: O(n) - Iterate through numbers from '1' to 'n'
Space Complexity: O(n) - Output list of size 'n'
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [
            'FizzBuzz' if i%15 == 0 else 
            'Buzz' if i%5 == 0 else
            'Fizz' if i%3 == 0 else 
            str(i) 
            for i in range(1,n + 1)
            ]
    
if __name__ == "__main__": # test_case run
    sol = Solution()
    n = 20
    print(sol.fizzBuzz(n)) 