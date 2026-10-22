# R
# Brute force would be N**2 where there would be a two loops, one loop to iterate thru each num in nums and an inner to check for a corresponding dupe. 
# T
# We instead optimize with a set() where we store each value seen previously with O(1) look up. 
# E
# def an empty set, loop once over each num - checking if we have seen it previously, if seen return true, else add num to our set.
# base case - return false post loop
# A
# Time complexity is O(n) iter + O(1) for set = O(n)
# Space is O(n) for worst case of no dupe and store all n nums.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        history = set()
        for num in nums:
            if num in history:
                return True
            history.add(num)
        return False
