class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_counts = {}

        # Build the hash map with character counts from s
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1

        # Subtract counts using characters from t
        for char in t:
            # If the character isn't in our map, or the count drops below 0, it's not an anagram
            if char_counts.get(char, 0) == 0:
                return False
            char_counts[char] -= 1

        return True