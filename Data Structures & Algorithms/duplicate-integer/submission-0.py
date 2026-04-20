class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #turn the occurences of the list to a hash map
        #the nums themselves will be keys, and the occurences of them will be the values
        #if any value in a KV pair > 1, then return true, else return false
        seen_nums = []
        for i in nums:
            if i in seen_nums:
                return True
            else:
                seen_nums.append(i)
        return False