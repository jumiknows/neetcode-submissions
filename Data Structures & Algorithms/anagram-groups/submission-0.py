from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict automatically creates an empty list if the key doesn't exist yet
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Create an array of 26 zeros to count frequencies of 'a' through 'z'
            count = [0] * 26
            
            for letter in word:
                # ord() gets the ASCII value. ord(letter) - ord('a') maps 'a' to 0, 'b' to 1, etc.
                count[ord(letter) - ord('a')] += 1
                
            # Convert the list to a tuple so it can be used as a dictionary key
            # e.g., "cat" and "act" both become (1, 0, 1, 0, ..., 1, 0...)
            anagram_map[tuple(count)].append(word)
            
        # Return just the grouped lists
        return list(anagram_map.values())