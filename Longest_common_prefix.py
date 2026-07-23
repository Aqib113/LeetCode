class Solution(object):
    def longestCommonPrefix(self, strs):
        commonPrefix  = ""
        minWord = len(min(strs))
        if len(strs) == 0:
            return commonPrefix
        for i in range(0,minWord):
            shouldAdd = True
            for eachStr in range(1,len(strs)):
                if strs[0][i] != strs[eachStr][i]:
                    shouldAdd = False
                    break
            if not shouldAdd:
                break
            commonPrefix += strs[0][i]
        return commonPrefix