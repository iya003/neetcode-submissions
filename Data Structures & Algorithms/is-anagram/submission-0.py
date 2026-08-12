class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False

sol = Solution()
s="jar"
t="jam"
result=sol.isAnagram(s,t)
print(result)