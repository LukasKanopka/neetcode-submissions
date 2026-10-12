class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        consolidatedList = set(nums)
        if len(consolidatedList) == len(nums):
            return False
        else:
            return True