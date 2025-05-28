"""
Solution 1 for Leetcode 383 - Ransom Note

Approach:
- Use two dictionaries (hashmaps) to count the frequency of each character 
  in ransomNote and magazine.
- Then, for each character in ransomNote, check if magazine has enough of it.

Time Complexity: O(n + m) - where 'n' is length of ransomNote, 'm' is length of magazine
Space Complexity: O(1) - Because the alphabet size is constant (only lowercase letters)
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_map_rn = {}
        for letter in ransomNote:
            letter_map_rn[letter] = letter_map_rn.get(letter, 0) + 1 

        letter_map_mag = {}
        for letter in magazine:
            letter_map_mag[letter] = letter_map_mag.get(letter, 0) + 1 

        for letter, count in letter_map_rn.items():
            if letter_map_mag.get(letter, 0) < count:
                return False            
        return True
