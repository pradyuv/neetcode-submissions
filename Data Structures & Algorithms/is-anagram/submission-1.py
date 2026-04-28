class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # the approach here would be to loop through a string 
        # and pop out letters from the other, and by the end if the other
        # string array is empty, then we have an anagram
        t_list= list(t)
        
        for i in s:
            if i in t_list:
                t_list.remove(i)
                
        
        return not t_list and len(s) == len(t)