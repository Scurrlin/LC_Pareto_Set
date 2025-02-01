class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Dictionary to group anagrams
        a_map = defaultdict(list)

        for w in strs:

            # Sort characters to create a unique key
            sorted_w = ''.join(sorted(w))

            # Group words by sorted key
            a_map[sorted_w].append(w)
        
        # Return grouped anagrams as a list
        return list(a_map.values())

# Time Complexity: O(N * K log K)
# Space Complexity: O(N * K)