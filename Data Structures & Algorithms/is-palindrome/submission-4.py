class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only alphanumeric characters from the original string
        clean_s = "".join([char for char in s if char.isalnum()]).lower()
        
        # A palindrome is equal to its own reverse
        return clean_s == clean_s[::-1]