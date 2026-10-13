class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = []
        for string in strs:
            hashmap = {}
            for letter in string:
                hashmap[letter] = hashmap.get(letter, 0) + 1
            maps.append(hashmap)

        groups = {}
        for i in range(len(maps)):
            key = tuple(sorted(maps[i].items()))
            
            if key not in groups: 
                groups[key] = [strs[i]]
            else: 
                groups[key].append(strs[i])

        res = []
        for key, values in groups.items():
            res.append(values)

        return res
                
            

