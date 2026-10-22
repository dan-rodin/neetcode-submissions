# R
# Determine whether s and t contain exactly the same characters 
# with exactly the same frequencies.

# T
# Brute force - for each character in s, scan through t to count/match its
# occurrences. This would take O(n**2) time.
#
# Better approach is to use hash maps to count the frequency of every character
# in both strings. Dictionary lookup/insertion is O(1) on avg, so both
# strings can be processed in O(n) time.

# E
# First, if the strings have different lengths, they cannot be anagrams.
# Then iterate through both strings at the same time.
# Store each character as a key and its frequency as the value.
# Finally, compare the two dictionaries.
# If they are equal, both strings contain the same characters with the
# same frequencies and therefore are anagrams.

# A
# Time Complexity: O(n)
# Space Complexity: O(n) in the general case for the two hash maps. Or actually 
# O(k) where k is num of distinct chars in lowercase alpha, so two dicts of 26
# chars is 52 entries, could prob do with one dict in 26 but ah well.

# Note: return sorted(s) == sorted(t) is shorter but slower O(n log n), 
# and Counter(s) == Counter(t) but too ez.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash, t_hash = {}, {}

        for i in range(0, len(s)):
            s_hash[s[i]] = s_hash.get(s[i], 0) + 1
            t_hash[t[i]] = t_hash.get(t[i], 0) + 1

        return s_hash == t_hash
