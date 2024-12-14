class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_int = str(x)
        reversed_str = string_int[::-1]  # Reverse the string using slicing
        return string_int == reversed_str