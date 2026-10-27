# If there are n strings and each has up to m characters
# Time: O(n * m)
# Space: O(1) auxiliary space

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""
        return prefix

