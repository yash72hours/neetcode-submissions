class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))  # Convert list to tuple
            dict1[key].append(s)

        return list(dict1.values())