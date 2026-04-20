class Solution:
    @staticmethod
    def normalize_string(s: str) -> str:
        return ''.join(ch.lower() for ch in s if ch.isalnum())

    def isPalindrome(self, s: str) -> bool:
        str_to_use = self.normalize_string(s)
        a = 0
        b = len(str_to_use) - 1
        while a < b:
            if str_to_use[a] == str_to_use[b]:
                a+=1
                b-=1
            else:
                return False
        return True

            