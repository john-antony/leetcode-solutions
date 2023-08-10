class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        partitions = []

        def dfs(i):
            if i >= len(s):
                res.append(partitions[::])
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    partitions.append(s[i:j+1])
                    dfs(j + 1)
                    partitions.pop()
        
        dfs(0)

        return res
    
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
        

        