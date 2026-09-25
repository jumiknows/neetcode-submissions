from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Sort the string and convert it directly to a tuple to use as a key
            # Example: "cat" -> ('a', 'c', 't')
            anagram_map[tuple(sorted(word))].append(word)
            
        return list(anagram_map.values())