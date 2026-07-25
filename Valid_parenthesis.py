class Solution(object):
    def isValid(self, s):
        types = {')':'(','}':'{',']':'['}
        values = types.values()
        stack = []
        for i in s:
            if i in values:
                stack.append(i)
            else:
                if len(stack)!=0 and stack[-1] == types[i]:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True    

a = Solution()
ans = a.isValid("]")
print(ans)