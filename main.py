class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_int = str(x)
        compare_str = ""
        for digit in string_int:
            compare_str = digit + compare_str
        if compare_str == string_int:
            return True
        else:
            return False