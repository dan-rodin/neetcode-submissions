# R
# We need to iterate thru list of nums and compare each num to each other num checking for target.
# Brute force would be O(n**2), looping over each num and using a nested loop to check against n-1 other nums checking for target.

# T
# More optimized; use a hash map - dict to store the history of prev nums to comare against

# E
# def a dict, use a for loop to iter thru nums list.
# Calc the complement that solves for the target, then check if its in the history dict.
# if not in dict break add dict(num: idx)
# if in dict return complement idx from hash map along with curr num idx in num

# A
# Since dict lookups are O(1) on average, reduces overall time complexity to O(n), using O(n) extra mem.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in history:
                return [history[complement], i]

            history[nums[i]] = i

# better solution:
def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i
