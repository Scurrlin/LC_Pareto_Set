class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a_map = defaultdict(list)

        for w in strs:
            sorted_w = ''.join(sorted(w))
            a_map[sorted_w].append(w)
        return list(a_map.values())

# Time Complexity: O(N * K log K)
# Space Complexity: O(N * K)