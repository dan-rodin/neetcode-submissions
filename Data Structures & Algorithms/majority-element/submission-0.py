# Brute force solution would be:
# for every element, scan the entire array and 
# count how many times it occurs.
# Time: O(n**2)
# Space: O(1)

# The best solution is the Boyer–Moore Voting Algorithm.
# Because the majority element occurs more than half the time, 
# you can effectively cancel every non-majority element against
# a majority element. The majority will survive.
# O(n) time
# O(1) space

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if candidate == num:
                count += 1
            else: 
                count -= 1

        return candidate
