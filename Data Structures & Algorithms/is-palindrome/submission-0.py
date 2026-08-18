class Solution:
    def isPalindrome(self, s: str) -> bool:

        main_s = ""

        for char in s:
            if char.isalnum():
                main_s += char
            

        low_s = main_s.lower()
        cleaned = "".join(low_s.split())

        rev_s = ""

        for i in range(len(cleaned)):
            rev_s = cleaned[i] +rev_s

        if rev_s == cleaned:
                return True
        else:
                return False
               
        