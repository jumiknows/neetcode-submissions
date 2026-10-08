class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed_txt = "".join(reversed(s))
        clean_reversed_txt = "".join([char for char in reversed_txt if char.isalnum()])
        clean_s = "".join([char for char in s if char.isalnum()])
        if (clean_reversed_txt.lower()==clean_s.lower()):
            return True
        else:
            return False