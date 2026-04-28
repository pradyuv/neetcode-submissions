class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # the approach here would be to loop through a string 
        # and pop out letters from the other, and by the end if the other
        # string array is empty, then we have an anagram
        if len(s) != len(t):
            return False

        count_t, count_s = {}, {}

        for i in range(len(s)):
            count_t[t[i]] = count_t.get(t[i], 0) + 1
            count_s[s[i]] = count_s.get(s[i], 0) + 1

        return count_t == count_s