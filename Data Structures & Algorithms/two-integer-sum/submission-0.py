class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we need to use a hash table somehow, but how?
        # how should I think about this problem
        nums_dict = {}
        for index, num in enumerate (nums):
            nums_dict[num] = index # KV pair, Key is Value of Array at the Value Index

        for i in range(len(nums)):
            difference = target - nums[i] # Calculate difference (what is needed)
            if difference in nums_dict and nums_dict[difference] != i: # if such difference exists in the hash map and isn't the current value itself
                return sorted([i, nums_dict[difference]]) #sort the indices
        return None