# Slightly better version from solutions O(n * k) time.

# R:
# Group words together if they contain the same characters with the same frequencies.

# T:
# Brute force would compare each word against every other word. > O(N**2)
# Better approach: Sort each word. Anagrams will produce the same sorted characters.
# Use that sorted result as a hashmap key.

# E:
# For each word, sort it and convert it to a tuple so it can be used as a key.
# Append the original word to the list stored under that key.

# A:
# if n = number of strings, k = average length if strings
# Because we sort each string... O(k log k)
# Time: O(n * k)
# Space: O(n * k) where k is aux space of freq dict

# Solutions
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            res[tuple(freq)].append(s)
        return list(res.values())

