class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            strNum = str(x)
            return strNum == strNum[::-1]