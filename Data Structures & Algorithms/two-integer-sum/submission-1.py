class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        complements = []
        for num in nums:
            complements.append(target-num)
        
        for i in range(len(complements)):
            if complements[i] in hashMap:
                return sorted([i, hashMap[complements[i]]])
            else:
                hashMap[nums[i]] = i
