# If there are n strings and each has up to m characters
# Time: O(n * m)
# Space: O(1) auxiliary space

# Vertical Scaling Solution...

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            char = strs[0][i]

            for word in strs[1:]:
                # word < prefix or prefix char not in word
                if i >= len(word) or word[i] != char:
                    return strs[0][:i]

        return strs[0]
