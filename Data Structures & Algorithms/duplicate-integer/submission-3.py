class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # transforms set to grab all unique values only
        check = set(nums)
        # find the length of unique values
        check_length = len(check)
        # if unique value length equals nums list length, return false
        if (check_length == len(nums)):
            return False
        # otherwise return true
        else:
            return True