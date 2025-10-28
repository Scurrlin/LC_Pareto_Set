class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for word in strs:
            sortedWord = ''.join(sorted(word))
            map[sortedWord].append(word)
        return list(map.values())

# Time Complexity: O(N * K log K)
# Space Complexity: O(N * K)