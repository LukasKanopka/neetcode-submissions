class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for string in strs: 
            count = [0] * 26
            
            for letter in string:
                index = ord(letter) - ord('a')
                count[index] += 1

            if tuple(count) in groups:
                groups[tuple(count)] = groups[tuple(count)] + [string]
            else: 
                groups[tuple(count)] = [string]

        res = []
        for value in groups.values():
            res.append(value)
        
        return res

            

